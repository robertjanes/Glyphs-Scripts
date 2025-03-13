# MenuTitle: Generate Numerators
# -*- coding: utf-8 -*-
__doc__ = """
Generate Numerators
"""
from GlyphsApp import GSComponent


# This seemed like the best logic for now.
# Not sure how else to calculate this.
def get_denominators_height():
    height = None
    for glyph in Font.glyphs:
        if ".numr" not in glyph.name:
            continue
        for layer in glyph.layers:
            if height is None or layer.bounds.size.height < height:
                height = layer.bounds.size.height
    return height


def create_numerators():
    height = get_denominators_height()

    for glyph in Font.glyphs:
        if ".numr" not in glyph.name:
            continue

        for layer in glyph.layers:
            layer.anchors = []
            dnom_glyph_name = glyph.name.replace(".numr", ".dnom")
            component = GSComponent(dnom_glyph_name)
            layer.shapes = [component]
            component.y = int(layer.master.capHeight - height)


def main():
    Font.disableUpdateInterface()
    create_numerators()
    Font.enableUpdateInterface()


main()
