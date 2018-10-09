#!/usr/bin/env python
# -*- coding: utf-8 -*-
#MenuTitle: Delete Background Layers
__doc__="""
Delete Background Layers
"""

Glyphs.clearLog()

for layer in Font.selectedLayers:
	layer.background.paths = []
