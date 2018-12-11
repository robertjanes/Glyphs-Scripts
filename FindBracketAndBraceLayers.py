#MenuTitle: Find Bracket and Brace Layers
# -*- coding: utf-8 -*-
__doc__="""
Find Bracket and Brace Layers
"""

import re
import GlyphsApp
Font = GlyphsApp.currentFont()

Glyphs.clearLog()

layerBraceReg = r".*?\{(\d+){1}(\,\s?\d+)*\}.*?"
layerBracketReg = r".*?\[(\d+){1}(\,\s?\d+)*\].*?"

braceLayers = []
bracketLayers = []

for glyph in Font.glyphs:
    for layer in glyph.layers:
        if layer.name is None: continue
        if re.match(layerBraceReg, layer.name) is not None: braceLayers.append(layer.name)
        if re.match(layerBracketReg, layer.name) is not None: bracketLayers.append(layer.name)

for layerName in braceLayers:
    print 'Brace Layer: ' + layerName

for layerName in bracketLayers:
    print 'Bracket Layer: ' + layerName
