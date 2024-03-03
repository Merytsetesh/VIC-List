# Loads VIC-20 programs saved in .PRG format and converts them to internal tokenised form, and
# saves programs as .PRG files.
#
# Internal token types are as follows:
#
#   TOKEN       VIC BASIC reserved word
#   QUOTE       Quotation marks, ". Value may be OPEN or CLOSE. We need this to know that any input
#               bytes with the high bits set are not tokens but characters.
#   QCHAR       A 'quoted character'; i.e. a character, not a token.
#   THING       Any other non-alphanumeric character.
#   INTEGER     Any integer value that is not a line number.
#   FLOAT       Any floating-point value, including scientific notation.
#   LINENUM     An integer value which is a line number. Detected by checking if the preceding
#               token is GOTO, GOSUB or THEN. (VIC BASIC allows omission of GOTO after THEN.)
#   ID          Any valid ID, including strings (...$) and integers (...%).
#
#
# Copyright (C) 2019 Simon Ellis.


import Types as Typ
import Characters as CH
import CharStream as CS

def Save(program, fname):
    data = [program.BasicStart.LowByte, program.BasicStart.HighByte]
    location = program.BasicStart.GetValue()

    for line in sorted(program.Code.keys()):
        linenum = Typ.Word(line)
        vals = [linenum.LowByte, linenum.HighByte]
        for tok in program.Code[line]:
            if tok[0] == "TOKEN":
                vals.append(int(tok[1]))
            elif tok[0] == "QUOTE":
                vals.append(34)
            elif tok[0] == "QCHAR":
                vals.append(int(CH.CharToNum(tok[1])))
            else:
                for i in range(len(tok[1])):
                    v = int(CH.CharToNum(tok[1][i]))
                    if not 0 <= v <= 256:
                        banana = 42
                    vals.append(v)
        vals.append(0)
        length = len(vals)
        location += length + 2
        jump = Typ.Word(location)
        vals.insert(0, jump.HighByte)
        vals.insert(0, jump.LowByte)
        data += vals
    data += [0, 0]
    with open(fname, 'wb') as f:
        f.write(bytes(data))
    f.close()


def Load(fname):
    cs = CS.CharStream()
    prog = Typ.Program()
    cs.Load(fname)
    prog.BasicStart.SetPair(cs.GetNextChar(), cs.GetNextChar())

    while not cs.EOF():
        next_lo = int(cs.GetNextChar())
        next_hi = int(cs.GetNextChar())

        if next_lo == 0 and next_hi == 0:
            break

        this_lo = int(cs.GetNextChar())
        this_hi = int(cs.GetNextChar())
        line_num = this_lo + 256 * this_hi

        toks = []

        string = ""
        state = 0
        last = 0

        ch = int(cs.GetNextChar())
        while ch > -1:
            if state == 0:
                if ch >= 128:                       #   detected a token: grab it and move on
                    last = ch
                    toks.append(["TOKEN", ch])

                elif ch == 34:                      #   found beginning of quoted text
                    toks.append(["QUOTE", "OPEN"])
                    state = 1

                elif 48 <= ch <= 57:                #   found a number: start grabbing it
                    string = chr(ch)
                    state = 2

                elif 65 <= ch <= 90:                #   found an ID: start grabbing it
                    string = chr(ch)
                    state = 3

                elif ch == 0:
                    break

                else:
                    toks.append(["THING", CH.NumToChar(ch)])            #   in case we have something not in ASCII

            elif state == 1:
                if ch == 0:
                    state = 0
                    cs.PushBack()
                if ch != 34:
                    toks.append(["QCHAR", CH.NumToChar(ch)])
                else:
                    toks.append(["QUOTE", "CLOSE"])
                    state = 0

            elif state == 2:
                if ch < 128 and chr(ch) in "0123456789+-.E":            #   only these valid in numbers
                    string += chr(ch)
                else:
                    cs.PushBack()
                    if "." not in string:
                        if last == 137 or last == 141 or last == 167:   #   GOTO, GOSUB or THEN
                            t = "LINENUM"
                        else:
                            t = "INTEGER"
                    else:
                        t = "FLOAT"
                    toks.append([t, string])
                    string = ""
                    state = 0

            elif state == 3:
                if 65 <= ch <= 90 or 48 <= ch <= 57:    #   IDs can contain letters & numbers
                    string += chr(ch)
                else:
                    if ch == 36 or ch == 37:            #   detect $ for strings and % for integers
                        string += chr(ch)
                    else:
                        cs.PushBack()                   #   end of ID
                    toks.append(["ID", string])
                    string = ""
                    last = None
                    state = 0

            if ch > -1:
                ch = int(cs.GetNextChar())

        prog.Code[line_num] = toks

    return prog
