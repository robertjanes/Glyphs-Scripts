# -*- coding: utf-8 -*-
# MenuTitle: Copy master child layers to master
__doc__ = """
Copy master child layers to master
"""
from vanilla import *
import ntpath

Glyphs.clearLog()


toFont = None
fromFont = None
toMaster = None
fromMaster = None


def getListOfAllMasters():
    allMasters = []
    for i, font in enumerate(Glyphs.fonts):
        for master in font.masters:
            allMasters.append(
                {
                    "fontIndex": i,
                    "name": master.name,
                    "id": master.id,
                    "gid": ntpath.basename(font.filepath) + " " + master.name,
                }
            )
    return allMasters


allMasters = getListOfAllMasters()


def getListOfAllMastersGids():
    allMastersGids = []
    for master in allMasters:
        allMastersGids.append(master["gid"])
    return allMastersGids


def isLayerMasterLayer(layer):
    return layer.layerId == layer.associatedMasterId


def copyGlyphChildLayersToGlyph(fromGlyph, toGlyph):
    # 	print fromGlyph, toGlyph
    for layer in fromGlyph.layers:
        # Skip master layers
        if isLayerMasterLayer(layer):
            continue
        # Skip layers that don't belong to our desired master
        if fromFont.masters[layer.associatedMasterId].name != fromMaster["name"]:
            continue

        # Append copy of layer into toGlyph layers
        # and assign correct master ID
        toGlyph.beginUndo()
        newLayer = layer.copy()
        newLayer.associatedMasterId = toMaster["id"]
        toGlyph.layers.append(newLayer)
        toGlyph.endUndo()


def copyMasterChildLayersToMaster(fromMasterIndex, toMasterIndex):
    global fromFont, toFont, fromMaster, toMaster
    fromMaster = allMasters[fromMasterIndex]
    toMaster = allMasters[toMasterIndex]
    fromFont = Glyphs.fonts[fromMaster["fontIndex"]]
    toFont = Glyphs.fonts[toMaster["fontIndex"]]

    for i, fromGlyph in enumerate(fromFont.glyphs):
        toGlyph = toFont.glyphs[fromGlyph.name]
        # Only copy layers if fromGlyph exits is in toFont
        if toGlyph:
            copyGlyphChildLayersToGlyph(fromGlyph, toGlyph)


class DialogWindow(object):
    def __init__(self):
        self.w = Window((400, 140), "Copy master child layers to master")
        self.w.fromMasterLabel = TextBox((10, 10, -10, 17), "From Font Master")
        self.w.fromMasterSelect = PopUpButton(
            (10, 30, -10, 20), getListOfAllMastersGids()
        )
        self.w.toMasterLabel = TextBox((10, 60, -10, 17), "To Font Master")
        self.w.toMasterSelect = PopUpButton(
            (10, 80, -10, 20), getListOfAllMastersGids()
        )
        self.w.myButton = Button(
            (10, 110, -10, 20), "Copy Layers", callback=self.buttonCallback
        )
        self.w.open()

    def buttonCallback(self, sender):
        # Display error if the to/from masters are the same
        if self.w.fromMasterSelect.get() == self.w.toMasterSelect.get():
            Message(
                "Copy master child layers to master",
                "'From Master' and 'To Master' must be different!'",
            )
            return
        self.w.close()
        # Run logic
        copyMasterChildLayersToMaster(
            self.w.fromMasterSelect.get(), self.w.toMasterSelect.get()
        )


DialogWindow()
