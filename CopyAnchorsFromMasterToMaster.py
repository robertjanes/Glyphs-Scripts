# -*- coding: utf-8 -*-
# MenuTitle: Copy anchors from master to master
__doc__ = """
Copy anchors from master to master
"""
from vanilla import *
import ntpath
import copy

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


def copyAnchorsFromLayerToLayer(fromLayer, toLayer):
    toLayer.anchors = copy.copy(fromLayer.anchors)


def copyAnchorsFromMasterToMaster(fromMasterIndex, toMasterIndex):
    global fromFont, toFont, fromMaster, toMaster
    fromMaster = allMasters[fromMasterIndex]
    toMaster = allMasters[toMasterIndex]
    fromFont = Glyphs.fonts[fromMaster["fontIndex"]]
    toFont = Glyphs.fonts[toMaster["fontIndex"]]

    for i, fromGlyph in enumerate(fromFont.glyphs):
        toGlyph = toFont.glyphs[fromGlyph.name]
        # Only copy layers if fromGlyph exits is in toFont
        if toGlyph:
            copyAnchorsFromLayerToLayer(
                fromGlyph.layers[fromMasterIndex], toGlyph.layers[toMasterIndex]
            )


class DialogWindow(object):
    def __init__(self):
        self.w = Window((360, 147), "Copy anchors from master to master")
        self.w.fromMasterLabel = TextBox((10, 10, -10, 17), "From Font Master")
        self.w.fromMasterSelect = PopUpButton(
            (10, 30, -10, 20), getListOfAllMastersGids()
        )
        self.w.toMasterLabel = TextBox((10, 60, -10, 17), "To Font Master")
        self.w.toMasterSelect = PopUpButton(
            (10, 80, -10, 20), getListOfAllMastersGids()
        )
        self.w.myButton = Button(
            (10, 114, -10, 20), "Copy Anchors", callback=self.buttonCallback
        )
        self.w.open()

    def buttonCallback(self, sender):
        # Display error if the to/from masters are the same
        if self.w.fromMasterSelect.get() == self.w.toMasterSelect.get():
            Message(
                "Copy anchors from master to master",
                "'From Master' and 'To Master' must be different!'",
            )
            return
        self.w.close()
        # Run logic
        copyAnchorsFromMasterToMaster(
            self.w.fromMasterSelect.get(), self.w.toMasterSelect.get()
        )


DialogWindow()
