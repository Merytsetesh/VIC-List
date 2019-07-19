# Sample program to demonstrate some of the functions of VIC-List.
#
# In order for the Print function to work you must have ReportLab installed *and* a font capable
# of displaying CBM characters. (See Print.py for more details.)
#
#
# Copyright (C) 2019 Simon Ellis.


import Renumber as RN
import List as L
import StreamPRG as SPRG
import StreamTXT as STXT
import Print as P


ProgDir  = "Progs"
ProgName = "alien overun"

# Load our program into memory...

prog = SPRG.Load(ProgDir + "/" + ProgName + ".prg")

# ... and show its internal tokenised form.

for l in prog.Code:
    print(l, prog.Code[l])

# Generate a text listing of it, and display it as we do so.

listing = L.List(prog, True)

# Renumber our program. Default is start 10, step 10.

RN.Renumber(prog)

# ... and list it again.

L.List(prog, True)

# Save it as a text file.

STXT.Save(prog, ProgName + ".txt")

# Load it again from this text file...

prog2 = STXT.Load(ProgName + ".txt")

# ... and list it again.

L.List(prog2, True)

# If you have not installed ReportLab and a CBM font, comment out the next line of code.

P.Print(prog2, ProgName + ".pdf")
