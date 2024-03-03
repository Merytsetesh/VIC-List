from reportlab.pdfgen import canvas
import reportlab.rl_config
reportlab.rl_config.warnOnMissingFontGlyphs = 1
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Font information

FontDir  = './Font'
FontName = 'PetMe2X.ttf'

FontSize = 8

INCH = 72

GlyphOffset = 0xE200

FontLead = int(FontSize * 1.25)
FontKern = int(FontSize * 2.25)

vicfont = TTFont('VICFont', FontDir + '/' + FontName)
pdfmetrics.registerFont(vicfont)
context = canvas.Canvas('00Stuff/Glyphs.pdf', pagesize=letter)
context.setFont('VICFont', FontSize)

TOP    = 10.75 * INCH
LEFT   =  1.50 * INCH

import Glyphs as G

chars = []
for c in range(30):
    chars += chr(c + 64)
chars[28] = "{UKP}"
chars.append("{UP-ARROW}")
chars.append("{LEFT-ARROW}")
for c in range(32):
    chars += chr(c + 32)


for r in range(2):
    posx = LEFT + (3.5 * INCH * r)

    for q in range(32):
            posy = TOP - ((q * FontLead * 2) + (q * 4))
            char = q + (32 * r)
            ch   = chars[char]

            gl = G.GetGlyph(ch) + GlyphOffset
            context.drawString(posx, posy, chr(gl))
            context.drawString(posx + INCH * 2.5, posy, chr(gl))

            for rev in range(2):
                reverse = False or rev == 1
                for low in range(2):
                    lower = False or low == 1

                    if "{" in ch:
                        ch = ch[1 : len(ch) - 1]

                    gl = G.GetGlyph(ch, reverse, lower)

                    shf   = "{SHF-" + ch + "}"
                    glshf = G.GetGlyph(shf, reverse, lower)

                    cbm   = "{CBM-" + ch + "}"
                    glcbm = G.GetGlyph(cbm, reverse, lower)

                    actx = posx + (rev *  INCH)
                    acty = posy - (low * FontLead)

                    context.drawString(actx + INCH * 0.5, acty, chr(gl + GlyphOffset))

                    if glshf > -1:
                        context.drawString(actx + INCH * 0.75, acty, chr(glshf + GlyphOffset))

                    if glcbm > -1:
                        context.drawString(actx + INCH, acty, chr(glcbm + GlyphOffset))


context.setFont('VICFont', 18)
st = "THE CBM VIC-20 CHARACTER SET"
for s in range(len(st)):
    context.drawString(INCH * 0.5, (10.5 * INCH) - (s * 24), st[s])

from reportlab.pdfbase.pdfmetrics import stringWidth

context.setFont('VICFont', 4)
st = "Made using VIC-List. VIC-List copyright (C) 2019 Merytsetesh."
w = stringWidth(st, 'VICFont', 4)
W = 8.5 * INCH

context.drawString((W - w) / 2, INCH / 8, st)

context.showPage()
context.save()

