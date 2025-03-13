# MenuTitle: Generate Denominators
# -*- coding: utf-8 -*-
__doc__ = """
Generate Denominators
"""
from GlyphsApp import GSComponent
from vanilla import *

DEFAULT_SCALE = 0.6


def create_denominators(scale=DEFAULT_SCALE):
    for glyph in Font.glyphs:
        if ".dnom" not in glyph.name:
            continue

        for layer in glyph.layers:
            layer.anchors = []
            layer.guides = []
            base_glyph_name = glyph.name.replace(".dnom", "")
            component = GSComponent(base_glyph_name)
            component.transform = (scale, 0, 0, scale, 0, 0)
            component.automaticAlignment = True
            layer.shapes = [component]
            layer.syncMetrics()
            layer.background = None
            layer.backgroundImage = None


def main(scale=DEFAULT_SCALE):
    Font.disableUpdateInterface()
    create_denominators(scale)
    Font.enableUpdateInterface()


class CreateDenominatorsDialog(object):
    def __init__(self):
        self.showErrors = True
        self.showWarnings = True
        self.w = Window((360, 70), "Create Denominators")
        self.w.textBox = TextBox((10, 10, 60, 17), "Scale")
        self.w.editText = EditText(
            (70, 10, -10, 22), text=DEFAULT_SCALE, callback=self.textBoxCallback
        )
        self.w.button = Button(
            (10, 40, -10, 20),
            "Create",
            callback=self.buttonCallback,
        )
        self.w.open()

    def buttonCallback(self, sender):
        scale = float(self.w.editText.get())
        if type(scale) is not float:
            raise ("Could not convert input to a flot")
        self.w.close()
        main(scale)

    def textBoxCallback(self, sender):
        pass


if __name__ == "__main__":
    CreateDenominatorsDialog()
