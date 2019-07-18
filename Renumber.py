# This provides something which was badly needed on the VIC: renumber! :-)
#
# This version can renumber all jump targets, including multiple targets after ON.
#
# Note that this function destructively modifies the code of the input program.
#
#
# Copyright (c) 2019 Simon Ellis.


# First creates a lookup table mapping current line numbers to their renumbered version. Next,
# each line is parsed for line numbers, as indicated by the LINENUM token type: tokens are simply
# added to a duplicate of the input line, but LINENUM tokens are replaced by the value in the
# lookup table.

def Renumber(program, start=10, step=10):
    if start < 0 or step <= 1 or (start + (step * (len(program.Code) - 1))) > 65535:
        return None
    lookup = {}
    line = start
    for k in sorted(program.Code.keys()):
        lookup[k] = line
        line += step

    line = start
    newcode = {}
    for k in sorted(program.Code.keys()):
        newline = []
        l = program.Code[k]
        for tok in l:
            if tok[0] != "LINENUM":
                newline.append(tok)
            else:
                newline.append(["LINENUM", str(lookup[int(tok[1])])])
        newcode[line] = newline
        line += step

    program.Code = newcode
