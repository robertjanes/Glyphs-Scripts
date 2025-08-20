# MenuTitle: Copy Uppercase to Lowercase
# -*- coding: utf-8 -*-
__doc__ = """
Copy Uppercase to Lowercase
"""

from GlyphsApp import GSLowercase, GSComponent
from utils import joinGlyphName


def copy_uppercase_to_lowercase(Font):
    Font.disableUpdateInterface()

    for glyphName in Font.glyphs.keys():
        glyph = Font.glyphs[glyphName]
        if glyph.category != "Letter":
            continue
        if glyph.case != GSLowercase:
            continue

        nameParts = glyphName.split(".")
        nameParts[0] = nameParts[0][0].upper() + nameParts[0][1:]
        uppercase_name = joinGlyphName(Font, nameParts)

        if uppercase_name in Font.glyphs:
            print(f"Copying {uppercase_name} to {glyphName}")
            for layer in glyph.layers:
                layer.shapes = [GSComponent(uppercase_name)]

    Font.enableUpdateInterface()


copy_uppercase_to_lowercase(Font)
