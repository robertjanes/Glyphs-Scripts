#!/usr/bin/env python
# -*- coding: utf-8 -*-
# MenuTitle: Half All Kerning Values
__doc__ = """
Half All Kerning Values
"""

for kernMasterId in Font.kerning:
    for leftGlyph in Font.kerning[kernMasterId]:
        for rightGlyph in Font.kerning[kernMasterId][leftGlyph]:
            Font.kerning[kernMasterId][leftGlyph][rightGlyph] = (
                Font.kerning[kernMasterId][leftGlyph][rightGlyph] / 2
            )
