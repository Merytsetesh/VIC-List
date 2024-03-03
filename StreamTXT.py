# Loads VIC-20 programs saved in text format and converts them to internal tokenised form, and
# saves programs as text files.
#
# This file uses a special REM at line 65535 (the last permitted line number in VIC BASIC) to
# store the beginning of BASIC for the program. This is required by PRG files, so it is maintained.
# Note that this information is not stored in the listing itself once it has been loaded, so it
# shouldn't appear in print-outs.
#
#
# Copyright (C) 2019 Merytsetesh.


import Types as Typ
import List as L
import ReservedWords as RW


# Saves a VIC-20 program in text format. Ensures that the start-of-BASIC pointer is maintained by
# creating line 65535 or, if it already exists, appending to it.

def Save(program, fname):
    temp = Typ.Program()
    for p in program.Code.keys():
        temp.Code[p] = program.Code[p]
    if 65535 in temp.Code.keys():
        temp.Code[65535].append(['THING', ":"])
    else:
        temp.Code[65535] = []
    temp.Code[65535].append(['TOKEN', RW.TokToNum("REM")])
    temp.Code[65535].append(['THING', "B@#" + str(program.BasicStart.GetValue())])
    with open(fname, 'w') as f:
        for l in L.List(temp):
            f.write(l + "\n")
    f.close()


# Load a VIC-20 program in VIC-List text format. Looks for start-of-BASIC information stored as a
# REM at line 65535 and removes it from the program if found.

def Load(fname):
    p = Typ.Program()
    loading = {}
    with open(fname) as f:
        c = f.readlines()
    f.close()

    for l in c:
        pos = 0
        while 48 <= ord(l[pos]) <= 57:
            pos += 1
        line_number = int(l[:pos + 1].strip())
        line = l[pos + 1:]
        if "B@#" in line:
            p.BasicStart.SetValue(int(line[line.index("#") + 1:]))
            continue

        state = 0
        last = None
        string = ""
        code = []
        pos = 0
        while pos < len(line):
            ch = line[pos]

            if state == 0:
                if 48 <= ord(ch) <= 57:             #   found a number: switch states
                    string += ch
                    state = 1
                elif ch == "{":                     #   found a special character so grab it for translation
                    string += ch
                    state = 2
                elif 65 <= ord(ch) <= 90:           #   found a text character: switch to check for ID or token
                    string += ch
                    state = 3
                elif ch == chr(34):                 #   found a quotation mark so switch state
                    code.append(["QUOTE", "OPEN"])
                    state = 4
                elif RW.MatchTokens(ch) == 1:       #   found a single-character token: encode as such
                    num = RW.TokToNum(ch)
                    code.append(["TOKEN", num])
                    last = num
                else:
                    if ch != '\n':
                        code.append(["THING", ch])

            elif state == 1:                        #   state to locate numbers
                if ch in "0123456789+-.E":
                    string += ch
                else:
                    pos -= 1
                    if "." not in string:
                        if last == 137 or last == 141 or last == 167:   #   GOTO, GOSUB or THEN
                            t = "LINENUM"
                        else:
                            t = "INTEGER"
                    else:
                        t = "FLOAT"
                    code.append([t, string])
                    string = ""
                    state = 0

            elif state == 2:                        #   recognise special characters *outside* quotation marks
                string += ch
                if ch == "}":
                    code.append(["THING", string.upper().strip()])
                    string = ""
                    state = 0

            elif state == 3:                        #   distinguish tokens from IDs
                if RW.MatchTokens(string + ch) == 1:       #   definitely a token
                    num = RW.TokToNum(string + ch)
                    code.append(["TOKEN", num])
                    last = num
                    string = ""
                    state = 0
                elif RW.MatchTokens(string + ch) == 0:       #   can't possibly be a token
                    pos -= 1
                    state = 5
                elif RW.MatchTokens(string + ch) == -1 or RW.MatchTokens(string + ch) > 1:
                    string += ch
                elif ch == "$" or ch == "%":        #   must be an ID: push back and let state 5 handle it
                    pos -= 1
                    state = 5
                elif 48 <= ord(ch) <= 57:             #   no digits in tokens: this MUST be an ID
                    string += ch
                    state = 5
#                    elif not ((48 <= ord(ch) <= 57) or (65 <= ord(ch) <= 90)):
                else:
                    pos -= 1
                    code.append(["ID", string])
                    string = ""
                    last = None
                    state = 0

            elif state == 4:                        #   recognise characters *inside* quotation marks
                if ch == chr(34):
                    code.append(["QUOTE", "CLOSE"])
                    string = ""
                    state = 0
                elif ch == "{":
                    string = ch
                    state = 6
                else:
                    code.append(["QCHAR", ch])

            elif state == 5:                        #   track characters in an ID
                if (48 <= ord(ch) <= 57) or (65 <= ord(ch) <= 90):
                    string += ch
                else:
                    if ch == "$" or ch == "%":
                        string += ch
                    else:
                        pos -= 1
                    code.append(["ID", string])
                    last = None
                    string = ""
                    state = 0

            elif state == 6:                        #   get special characters inside quotes
                string += ch
                if ch == "}":
                    code.append(["QCHAR", string.upper().strip()])
                    string = ""
                    state = 4

            pos += 1

        loading[line_number] = code

    p.Code = loading
    return p