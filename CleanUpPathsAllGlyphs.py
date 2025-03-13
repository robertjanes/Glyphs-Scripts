# MenuTitle: Clean Up Paths All Glyphs
# -*- coding: utf-8 -*-
__doc__ = """
Clean Up Paths All Glyphs
"""
from GlyphsApp import Glyphs

Font = Glyphs.font

for glyph in Font.glyphs:
    for layer in glyph.layers:
        layer.cleanUpPaths()
