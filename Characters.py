# Converts from .PRG symbols to human-readable symbols.
# HRSs are contained in {...}, with the exception of [ and ], which map directly to characters.
#
#
# Copyright (C) 2019 Merytsetesh.


Characters = {   5 : "{WHI}",
                13 : "{RETURN}",
                17 : "{CRSR-DOWN}",
                18 : "{RVS-ON}",
                19 : "{HOME}",
                20 : "{DEL}",
                28 : "{RED}",
                29 : "{CRSR-RIGHT}",
                30 : "{GRN}",
                31 : "{BLU}",
                91 : "[",
                92 : "{UKP}",
                93 : "]",
                94 : "{UP-ARROW}",
                95 : "{LEFT-ARROW}",
                96 : "{SHF-*}",
               123 : "{SHF-+}",
               124 : "{CBM--}",
               125 : "{SHF--}",
               126 : "{SHF-UP-ARROW}",
               127 : "{CBM-*}",
               133 : "{F1}",
               134 : "{F3}",
               135 : "{F5}",
               136 : "{F7}",
               137 : "{F2}",
               138 : "{F4}",
               139 : "{F6}",
               140 : "{F8}",
               141 : "{SHF-RTRN}",
               144 : "{BLK}",
               145 : "{CRSR-UP}",
               146 : "{RVS-OFF}",
               147 : "{CLR}",
               148 : "{INST}",
               156 : "{PUR}",
               157 : "{CRSR-LEFT}",
               158 : "{YEL}",
               159 : "{CYN}",
               160 : "{SHF-SPC}",
               161 : "{CBM-K}",
               162 : "{CBM-I}",
               163 : "{CBM-T}",
               164 : "{CBM-@}",
               165 : "{CBM-G}",
               166 : "{CBM-+}",
               167 : "{CBM-M}",
               168 : "{CBM-UKP}",
               169 : "{SHF-UKP}",
               170 : "{CBM-N}",
               171 : "{CBM-Q}",
               172 : "{CBM-D}",
               173 : "{CBM-Z}",
               174 : "{CBM-S}",
               175 : "{CBM-P}",
               176 : "{CBM-A}",
               177 : "{CBM-E}",
               178 : "{CBM-R}",
               179 : "{CBM-W}",
               180 : "{CBM-H}",
               181 : "{CBM-J}",
               182 : "{CBM-L}",
               183 : "{CBM-Y}",
               184 : "{CBM-U}",
               185 : "{CBM-O}",
               186 : "{SHF-@}",
               187 : "{CBM-F}",
               188 : "{CBM-C}",
               189 : "{CBM-X}",
               190 : "{CBM-V}",
               191 : "{CBM-B}"
              }

def NumToChar(num):
    if 192 <= num <= 223:
        num -= 96
    if 224 <= num <= 254:
        num -= 64
    if num == 255:
        num = 126
    if 97 <= num <= 122:
        return "{SHF-" + chr(num - 32) + "}"
    if num in Characters.keys():
        return Characters[num]
    return chr(num)

def CharToNum(char):
    if "{" not in char:
        return ord(char)
    if char[:4] == "{SHF":
        ch = ord(char[5])
        if 65 <= ch <= 90:
            return ch
    ch = char.upper()
    for k in Characters.keys():
        if Characters[k] == ch:
            return k
    return None