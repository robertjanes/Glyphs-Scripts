# -*- coding: utf-8 -*-
# MenuTitle: ↹ Swap Glyph Names
__doc__ = """
Swap Glyph Names
"""

selectedLayers = Glyphs.font.selectedLayers


def main(selectedLayers):
    # Don't swap if more/less than 2 layers are selected
    if len(selectedLayers) != 2:
        return

    glyphOne = selectedLayers[0].parent
    glyphTwo = selectedLayers[1].parent

    glyphOneName = glyphOne.name
    glyphTwoName = glyphTwo.name

    glyphOne.name = "_" + glyphTwoName + "_"
    glyphTwo.name = glyphOneName
    glyphOne.name = glyphTwoName

    # Update unicodes
    glyphOne.updateGlyphInfo(True)
    glyphTwo.updateGlyphInfo(True)


main(selectedLayers)
