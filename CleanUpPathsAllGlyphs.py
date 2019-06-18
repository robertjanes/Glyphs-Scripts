#MenuTitle: Clean Up Paths All Glyphs
# -*- coding: utf-8 -*-
__doc__="""
Clean Up Paths All Glyphs
"""
import GlyphsApp
Font = GlyphsApp.currentFont()
for glyph in Font.glyphs:
	for layer in glyph.layers:
		layer.cleanUpPaths()
