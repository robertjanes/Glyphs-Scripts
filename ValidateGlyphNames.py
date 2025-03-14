# MenuTitle: Validate Glyph Names
# -*- coding: utf-8 -*-
__doc__ = """
Validate Glyph Names
"""


def validateGlyphName(name):
    name = name.replace(".tf", ".tnum")
    name = name.replace(".sc", ".c2sc")
    nameSplit = name.split(".")
    fontFeatures = [f.name for f in Font.features]
    previousParts = []
    for n, namePart in enumerate(nameSplit):
        if n > 0:
            if namePart not in fontFeatures:
                continue
            indexInFeatures = fontFeatures.index(namePart)
            for previousPart in previousParts[1:]:
                if previousPart not in fontFeatures:
                    continue
                prevoiousIndexInFeatures = fontFeatures.index(previousPart)
                if indexInFeatures < prevoiousIndexInFeatures:
                    return False
        previousParts.append(namePart)
    return True


invalidGlyphNames = []
for glyph in Font.glyphs:
    if validateGlyphName(glyph.name) is False:
        invalidGlyphNames.append(glyph.name)

if len(invalidGlyphNames) > 0:
    print("Found %s invalid glyph names:" % (len(invalidGlyphNames)))
    for invalidGlyphName in invalidGlyphNames:
        print("— %s" % (invalidGlyphName))
else:
    print("No invalid glyph names found.")
