# MenuTitle: Generate Small Caps
# -*- coding: utf-8 -*-
__doc__ = """
Generate Small Caps
"""

from GlyphsApp import GSGlyph, GSUppercase
from utils import joinGlyphName


def createSmallCaps(Font):
    Font.disableUpdateInterface()

    for glyphName in Font.glyphs.keys():
        glyph = Font.glyphs[glyphName]
        if glyph.category != "Letter":
            continue
        if glyph.case != GSUppercase:
            continue

        nameParts = glyphName.split(".")
        nameParts[0] = nameParts[0].lower()
        nameParts.append("sc")
        glyphScName = joinGlyphName(Font, nameParts)

        if glyphScName not in Font.glyphs:
            glyphSc = GSGlyph(glyphScName)
            Font.glyphs.append(glyphSc)

    Font.enableUpdateInterface()


createSmallCaps(Font)
