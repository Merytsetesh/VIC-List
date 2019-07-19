# Translates a tokenised program into a human-readable listing and outputs it as a list containing
# the individual lines.
#
# Optionally displays the listing to stdout.
#
#
# Copyright (C) 2019 Simon Ellis.

import ReservedWords as RW

def List(program, display=False):
    lst = []
    for k in sorted(program.Code.keys()):
        line = program.Code[k]
        out = str(k) + " "
        for tok in line:
            if tok[0] == "TOKEN":
                out += RW.NumToTok(tok[1])
            elif tok[0] == "QUOTE":
                out += chr(34)
            else:
                out += tok[1]
        lst.append(out)
        if display:
            print (out)
    return lst