#MenuTitle: Close Open Corners
# -*- coding: utf-8 -*-
__doc__="""
Close Open Corners
"""
import GlyphsApp
Font = GlyphsApp.currentFont()

Glyphs.clearLog()
from GlyphsApp import GSPathPen

for glyph in Font.glyphs:
    for layer in glyph.layers:
        thisLayer = layer

        layerPaths = [l for l in thisLayer.paths]

        thisLayer.paths = []

        for eachPath in layerPaths:
            pen = GSPathPen.alloc().init()
            eachPath.drawInPen_(pen)
            eachPath = pen.layer().paths
            eachPath = eachPath[0]
            thisLayer.addPath_(eachPath)
            # thisLayer.cleanUpPaths()
