# MenuTitle: Close Open Corners
# -*- coding: utf-8 -*-
__doc__ = """
Close all open corners in the current font.
"""
Glyphs.clearLog()
from GlyphsApp import GSPathPen, GSPath
import copy

for glyph in Font.glyphs:
    for layer in glyph.layers:
        newShapes = []
        for s, shape in enumerate(layer.shapes):
            if isinstance(shape, GSPath) is False:
                newShapes.append(shape)
                continue
            pen = GSPathPen.new()
            path = copy.copy(shape)
            path.drawInPen_(pen)
            path = pen.layer().paths[0]
            newShapes.append(path)
        layer.shapes = newShapes
