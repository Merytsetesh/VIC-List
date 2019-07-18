# Contains a list of all the reserved words in standard VIC BASIC, plus lookup functions.
#
#
# Copyright (C) 2019 Simon Ellis.


# List of reserved words in VIC-20 BASIC, in order of token value.

Reserved = [ "END",
             "FOR",
             "NEXT",
             "DATA",

             "INPUT#",
             "INPUT",
             "DIM",
             "READ",

             "LET",
             "GOTO",
             "RUN",
             "IF",

             "RESTORE",
             "GOSUB",
             "RETURN",
             "REM",

             "STOP",
             "ON",
             "WAIT",
             "LOAD",

             "SAVE",
             "VERIFY",
             "DEF",
             "POKE",

             "PRINT#",
             "PRINT",
             "CONT",
             "LIST",

             "CLR",
             "CMD",
             "SYS",
             "OPEN",

             "CLOSE",
             "GET",
             "NEW",
             "TAB(",

             "TO",
             "FN",
             "SPC(",
             "THEN",

             "NOT",
             "STEP",
             "+",
             "-",

             "*",
             "/",
             "",
             "AND",
             "OR",
             ">",
             "=",
             "<",
             "SGN",
             "INT",
             "ABS",
             "USR",
             "FRE",
             "POS",
             "SQR",
             "RND",
             "LOG",
             "EXP",
             "COS",
             "SIN",
             "TAN",
             "ATN",
             "PEEK",
             "LEN",
             "STR$",
             "VAL",
             "ASC",
             "CHR$",
             "LEFT$",
             "RIGHT$",
             "MID$",
             "GO"
            ]


# Backtranslate from a number to a string. All tokens are single characters with the high bit set.

def NumToTok(number):
    if number >= 128 and number <= (128 + len(Reserved)):
        return Reserved[number - 128]
    return None


# Check to see if an input string matches a reserved word and output the token for it.

def TokToNum(tok):
    if tok in Reserved:
        return Reserved.index(tok) + 128
    return None


# I think the way CBM BASIC tokenises input is by looking for a first-match algorithm; this
# assumption is based on the fact that you can't have certain identifiers (e.g. OR) and that
# sometimes spaces are required between reserved words and identifiers. This function attempts to
# determine how many possible reserved words exist with a given prefix.
#
# I could make this faster with a trie, but I'm not going to. (For now.)

def MatchTokens(input):
    if not input:
        return None
    tok = input.upper()     #   all tokens are stored in upper case.
    possible = []
    l = len(tok)
    for r in Reserved:
        if r[:l] == tok:
            possible.append(r)
    if len(possible) == 0:
        return 0
    elif len(possible) > 1:
        return len(possible)
    elif tok != possible[0]:
        return -1
    else:
        return 1
