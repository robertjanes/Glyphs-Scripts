# MenuTitle: Generate Circled Figures
# -*- coding: utf-8 -*-
__doc__ = """
Generate Circled Figures
"""
from GlyphsApp import GSComponent, GSGlyph
import re

numerator_scale = 1.1
circled_figures_circled_part_glyph_name = "_part.circled"
circled_figures_black_circled_part_glyph_name = "_part.blackCircled"
circled_figures_glyph_names = [
    "zero.blackCircled",
    "one.blackCircled",
    "two.blackCircled",
    "three.blackCircled",
    "four.blackCircled",
    "five.blackCircled",
    "six.blackCircled",
    "seven.blackCircled",
    "eight.blackCircled",
    "nine.blackCircled",
    "zero.circled",
    "one.circled",
    "two.circled",
    "three.circled",
    "four.circled",
    "five.circled",
    "six.circled",
    "seven.circled",
    "eight.circled",
    "nine.circled",
]


def create_circled_figures():

    if Font.glyphs[circled_figures_circled_part_glyph_name] == None:
        glyph_part_circled = GSGlyph(circled_figures_circled_part_glyph_name)
        Font.glyphs.append(glyph_part_circled)

    if Font.glyphs[circled_figures_black_circled_part_glyph_name] == None:
        glyph_part_black_circled = GSGlyph(
            circled_figures_black_circled_part_glyph_name
        )
        Font.glyphs.append(glyph_part_black_circled)

    for glyph_name in circled_figures_glyph_names:
        glyph = Font.glyphs[glyph_name]
        if Font.glyphs[glyph_name] == None:
            glyph = GSGlyph(glyph_name)
            Font.glyphs.append(glyph)

        dnom_component_name = re.sub("(.circled|.blackCircled)", ".dnom", glyph_name)
        circled_component_name = (
            circled_figures_circled_part_glyph_name
            if ".circled" in glyph_name
            else circled_figures_black_circled_part_glyph_name
        )

        for layer in glyph.layers:
            layer.anchors = []
            circle_component = GSComponent(circled_component_name)
            dnom_component = GSComponent(dnom_component_name)
            dnom_component.transform = (numerator_scale, 0, 0, numerator_scale, 0, 0)
            circle_component.automaticAlignment = True
            dnom_component.automaticAlignment = True
            layer.shapes = [circle_component, dnom_component]


def main():
    Font.disableUpdateInterface()
    create_circled_figures()
    Font.enableUpdateInterface()


main()
