# Converts special symbols into the correct glyph in the VIC font; e.g. {HOME} maps to an inverse S.
#
# One note: I'm not entirely sure that the mapping for {CRSR-LEFT} is correct. It's hard to tell
# on the old listings which vertical line is blank; that these glyphs aren't contiguous in the
# font, or in the character ROM, only exacerbates the issue. If I've got this wrong then I'm
# happy to be corrected. Equally, if I've missed the mark with others [urk! :-( ].
#
#
# Copyright (C) 2019 Simon Ellis.


REV_BYTE  = 128
LOW_BYTE  = 256


# Indicates a non-printable or invalid glyph.

NOGLYPH   =  -1


# This dictionary contains mappings for special VIC control characters (upper block) and shifted
# non-alphabetic characters (second block). Control characters map to symbols in the reverse block.
#
# As the return character isn't displayed,

Special =     { "{WHI}"          : 133,
                "{RETURN}"       : NOGLYPH,
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
                "{SHF-RTRN}"     : NOGLYPH,
                "{BLK}"          : 207,
                "{CRSR-UP}"      : 209,
                "{RVS-OFF}"      : 210,
                "{CLR}"          : 211,
                "{INST}"         : 212,
                "{PUR}"          : 220,
                "{CRSR-LEFT}"    : 221,
                "{YEL}"          : 222,
                "{CYN}"          : 223,

                "{CBM-+}"        : 102,
                "{SHF-+}"        :  91,
                "{CBM--}"        :  92,
                "{SHF--}"        :  93,
                "{CBM-UKP}"      : 104,
                "{SHF-UKP}"      : 105,
                "{CBM-@}"        : 100,
                "{SHF-@}"        : 122,
                "{CBM-*}"        :  95,
                "{SHF-*}"        :  64,
                "{SHF-UP-ARROW}" :  94,
                "{CBM-UP-ARROW}" :  94
              }


# The block character set reached using the Commodore key is a pain. The ordering of the characters
# in the glyphset follows no logic I can see. No number keys map to CBM symbols, and only some of
# the non-alpha ones. Shift-Up-Arrow and CBM-Up-Arrow map to the same symbol.
#
# This string maps from an alpha character to a CBM glyph in the range 96-127. Spaces are caused
# by symbols in the dictionary above mapping to that codepoint.

CBMLETTERS = " KIT G M  NQDZSPAERWHJLYUO FCXVB"


# Some ASCII symbols do not have block graphics. These require special handling.

NOGRAPHICS = " !\"#$%&'()*+,-./0123456789:;<=>?"


def GetGlyph(sym, reverse=False, lower=False):
    sym = sym.upper()
    offset = 0
    glyph = NOGLYPH

    if sym in Special.keys():
        glyph = Special[sym]
    else:
        if "SHF" in sym or "CBM" in sym:
            c = sym[5]
            if "SHF" in sym:
                offset = 64
            if "CBM" in sym:
                offset = 96
        else:
            c = sym

        if '[' in c or ']' in c or c in NOGRAPHICS:
            if offset != 0:
                glyph = NOGLYPH
            else:
                if "[" in c:
                    glyph = 27
                elif "]" in c:
                    glyph = 29
                else:
                    glyph = 32 + NOGRAPHICS.index(c)

        elif "UKP" in sym or "ARROW" in sym:
            if "UKP" in sym:
                glyph = 28
            elif "UP-ARROW" in sym:
                if offset != 96:
                    glyph = 30
            elif "LEFT-ARROW" in sym:
                if offset == 0:
                    glyph = 31

        elif offset == 96:
            if len(sym) > 7 or c not in CBMLETTERS:
                glyph = NOGLYPH
            else:
                glyph = CBMLETTERS.index(c)

        elif 64 <= ord(c) <= 90:
            glyph = ord(c) - 64

    if glyph != NOGLYPH:
        if glyph < 129 and reverse:
            glyph += REV_BYTE
        if lower:
            glyph += LOW_BYTE
        return glyph + offset

    return NOGLYPH
