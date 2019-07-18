# Converts special symbols into the correct glyph in the VIC font; e.g. {HOME} maps to an inverse S.
#
# One note: I'm not entirely sure that the mapping for {CRSR-LEFT} is correct. It's hard to tell
# on the old listings which vertical line is blank; that these glyphs aren't contiguous in the
# font, or in the character ROM, only exacerbates the issue. If I've got this wrong then I'm
# happy to be corrected. Equally, if I've missed the mark with others [urk! :-( ].
#
#
# Simon Ellis, 2019.


REVERSE   = 0
REV_BYTE  = 128
LOWERCASE = 0
LOW_BYTE  = 256


Special =     { "{WHI}"          : 133,
                "{RETURN}"       :  -1,
                "{CRSR-DOWN}"    : 145,
                "{RVS-ON}"       : 146,
                "{HOME}"         : 147,
                "{DEL}"          : 148,
                "{RED}"          : 156,
                "{CRSR-RIGHT}"   : 157,
                "{GRN}"          : 158,
                "{BLU}"          : 159,
                "{F1}"           : 197,
                "{F3}"           : 198,
                "{F5}"           : 199,
                "{F7}"           : 200,
                "{F2}"           : 201,
                "{F4}"           : 202,
                "{F6}"           : 203,
                "{F8}"           : 204,
                "{SHF-RTRN}"     :  -1,
                "{BLK}"          : 207,
                "{CRSR-UP}"      : 209,
                "{RVS-OFF}"      : 210,
                "{CLR}"          : 211,
                "{INST}"         : 212,
                "{PUR}"          : 220,
                "{CRSR-LEFT}"    : 221,
                "{YEL}"          : 222,
                "{CYN}"          : 223,
              }


def GetGlyph(sym):
    sym = sym.upper()
    offset = 0

    if sym in Special.keys():
        glyph = Special[sym]
    else:
        if "SHF" in sym:
            offset = 64
        elif "CBM" in sym:
            offset = 96

        if offset > 0:
            c = sym[5]
        else:
            c = sym

        glyph = 0
        if "UKP" in sym:
            glyph = 28
        elif "UP-ARROW" in sym:
            glyph = 30
        elif "LEFT-ARROW" in sym:
            glyph = 31
        elif "[" in sym:
            glyph = 27
        elif "]" in sym:
            glyph = 29
        elif 64 <= ord(c) <= 90:
            glyph = ord(c) - 64
        elif c in " !\"#$%&'()*+,-./0123456789:;<=>?":
            glyph = 32 + " !\"#$%&'()*+,-./0123456789:;<=>?".index(sym)
        else:
            glyph = -1

    if glyph > -1:
        if glyph < 129 and REVERSE == 1:
            glyph += REV_BYTE

        if LOWERCASE == 1:
            glyph += (LOWERCASE * LOW_BYTE)

    return glyph + offset
