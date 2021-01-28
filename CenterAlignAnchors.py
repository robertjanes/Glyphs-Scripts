#MenuTitle: Center Align Anchors
# -*- coding: utf-8 -*-
__doc__="""
Center Align Anchors
"""
from GlyphsApp import NSPoint

layer = Font.selectedLayers[0]

for anchor in layer.anchors:
	if anchor.selected:
		anchor.position = NSPoint(int(layer.width / 2), anchor.position.y)