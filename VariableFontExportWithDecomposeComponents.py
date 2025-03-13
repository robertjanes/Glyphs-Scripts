# -*- coding: utf-8 -*-
# MenuTitle: Variable Font Export with Decompose Components
__doc__ = """
Variable Font Export with Decompose Components
"""
import GlyphsApp
import copy

font = Glyphs.font

Glyphs.clearLog()


def main():
    # Copy all layers to backup
    for master in font.masters:
        for glyph in font.glyphs:
            masterLayer = glyph.layers[master.id]

            # We can ignore layers with no components
            if len(masterLayer.components) == 0:
                continue

            # Duplicate master layer to backup
            newLayer = masterLayer.copy()
            newLayer.name = "_VariableFontExportTempLayer"
            glyph.layers.append(newLayer)
            # Decompose master layer
            masterLayer.decomposeComponents()

    # Export the variable font
    Glyphs.font.export(Format=VARIABLE, FontPath=saveLocation)
    Glyphs.showNotification(
        "Export Variable Font",
        "The export of %s was successful." % (Glyphs.font.familyName),
    )

    # Restore original layers
    for master in font.masters:
        for glyph in font.glyphs:
            masterLayer = glyph.layers[master.id]
            # Only need to restore layers with components
            if glyph.layers["_VariableFontExportTempLayer"] is not None:
                backupLayer = glyph.layers["_VariableFontExportTempLayer"]
                newLayer = copy.copy(backupLayer)
                newLayer.layerId = master.id
                glyph.layers[master.id] = newLayer
                # Deletes '_VariableFontExportTempLayer'
                del glyph.layers[-1]


saveLocation = GlyphsApp.GetFolder()
if saveLocation is not None:
    main()
