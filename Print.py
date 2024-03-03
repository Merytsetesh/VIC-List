# =================================================================================================
#
#           This program requires the ReportLab module to be installed in order to run.
#           ---------------------------------------------------------------------------
#
# =================================================================================================
#
#          This program assumes you have a font capable of displaying PETSCII characters.
#          ------------------------------------------------------------------------------
#
# I found an excellent set of *free* CBM fonts at the KreativeKorp website, and I used these to
# develop this software. They are available here:
#
#                     http://www.kreativekorp.com/software/fonts/c64.shtml
#
# =================================================================================================
#
# Takes a VIC-List program and generates a PDF of a listing for it.
#
#
# Copyright (C) 2019 Merytsetesh.


from reportlab.pdfgen import canvas
import reportlab.rl_config
reportlab.rl_config.warnOnMissingFontGlyphs = 0
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


# There are 72 points (pt) in an inch.

INCH    = 72


# Define the page information. Change the RHS of PageSize to your preferred paper size.
#
# IMPORTANT: ReportLab page sizes are stored internally in points.

PageSize = letter
size     = reportlab.lib.pagesizes.portrait(PageSize)
HEIGHT   = size[1]
WIDTH    = size[0]


# ReportLab uses computer graphics conventions, i.e. (0, 0) is at the bottom-left of the page.

TOP    = HEIGHT
RIGHT  = WIDTH

MARGIN = INCH

TopMargin    = TOP - MARGIN
LeftMargin   = MARGIN
RightMargin  = RIGHT - MARGIN
BottomMargin = MARGIN


# Font information

FontDir  = './Font'
FontName = 'PetMe.ttf'

FontSize = 8


# We use the glyphs directly and paint them one at a time to the PDF canvas. This value points to
# where the full 8K character set resides in the TTF as a continuous block.

GlyphOffset = 0xE200


# Takes a VIC-List program and turns it into a stream of glyphs. First the program is LISTed, then
# we go through the listing and turn any special characters (e.g. {RED}, {CBM-D}) into the correct
# VIC special character. The whole program is represented by a list of strings of characters, one
# per program line.

def Englyph(program):
    import Glyphs as G, List as L
    listing = L.List(program)
    output = []
    for line in listing:
        glyphs = []
        pos = 0
        gl = -1
        while pos < len(line):
            if line[pos] != "{":
                gl = G.GetGlyph(line[pos])
                pos += 1
            elif line[pos] == "{":
                sym = ""
                while line[pos] != "}":
                    sym += line[pos]
                    pos += 1
                sym += "}"
                gl = G.GetGlyph(sym)
            if gl > -1:
                glyphs.append(gl)
        output.append(glyphs)
    return output


# Creates a PDF of a VIC-20 program listing.
#
# Leading is the space between lines. Experimentation showed that a leading of 1.33333 gave good
# readability. Using a double-height font will require this to be doubled.
#
# Kerning is the space between letters on the same line. I found that the wider VIC fonts required
# manual adjustment of kerning to make sure that they were readable. This value will need to be
# adjusted if using a wider font (e.g. * 2 if using a 2X font).

def Print(program, filename="Listing.pdf"):
    output = Englyph(program)

    FontLead = int(FontSize * 1.3333333)
    FontKern = FontSize

    vicfont = TTFont('VICFont', FontDir + '/' + FontName)
    pdfmetrics.registerFont(vicfont)
    context = canvas.Canvas(filename, pagesize=PageSize)

    CursorX = LeftMargin
    CursorY = TopMargin
    context.setFont('VICFont', FontSize)
    for line in output:
        for glyph in line:
            num = glyph + GlyphOffset
            char = chr(num)
            context.drawString(CursorX, CursorY, char)
            CursorX += FontKern
            if CursorX > RightMargin:
                CursorX = LeftMargin
                CursorY -= FontLead
                if CursorY < BottomMargin:
                    context.showPage()
                    context.setFont('VICFont', FontSize)
                    CursorY = TopMargin
        if CursorX > LeftMargin:
            CursorX = LeftMargin
            CursorY -= FontLead
        if CursorY < BottomMargin:
            context.showPage()
            context.setFont('VICFont', FontSize)
            CursorY = TopMargin
    context.showPage()
    context.save()
