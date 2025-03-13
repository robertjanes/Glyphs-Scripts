#!/usr/bin/env python
# -*- coding: utf-8 -*-
# MenuTitle: Delete Background Layers
__doc__ = """
Delete Background Layers
"""

from GlyphsApp import Glyphs

Font = Glyphs.font


def delete_background_layers():
    for layer in Font.selectedLayers:
        layer.background.paths = []


if __name__ == "__main__":
    delete_background_layers()
