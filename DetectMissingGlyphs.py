# MenuTitle: Detect Missing Glyphs
# -*- coding: utf-8 -*-
__doc__ = """
Detect Missing Glyphs
"""
from GlyphsApp import Glyphs
from utils import joinGlyphName
import re

FEATURE_REGEX = r".(cv\d\d|ss\d\d)"


def get_base_feature_glyphs_pairs(Font):
    base_feature_glyphs = []
    base_feature_glyphs_pairs = {}
    for glyph in Font.glyphs:
        if re.search(FEATURE_REGEX, glyph.name) is not None:
            # for component in glyph.layers[0].components:
            #     match = re.search(FEATURE_REGEX, component.componentName)
            #     if match is not None:
            #         feature = match.group(1)
            #         base_component_glyph_name = re.sub(
            #             FEATURE_REGEX, "", component.componentName
            #         )
            #         if Font.glyphs[base_component_glyph_name] is None:
            #             continue
            #         if component.componentName not in base_feature_glyphs:
            #             base_feature_glyphs_pairs[base_component_glyph_name] = (
            #                 component.componentName
            #             )
            #             base_feature_glyphs.append(component.componentName)
            match = re.search(FEATURE_REGEX, glyph.name)
            if match is not None:
                feature = match.group(1)
                base_glyph_name = re.sub(FEATURE_REGEX, "", glyph.name, count=1)
                if Font.glyphs[base_glyph_name] is None:
                    continue
                if glyph.name not in base_feature_glyphs:
                    base_feature_glyphs_pairs[base_glyph_name] = glyph.name
                base_feature_glyphs.append(glyph.name)

    return base_feature_glyphs_pairs


def detect_missing_glyphs():
    base_feature_glyphs_pairs = get_base_feature_glyphs_pairs(Glyphs.font)
    # print(base_feature_glyphs_pairs)
    missing_glyphs = []

    for glyph in Font.glyphs:
        for component in glyph.layers[0].components:
            if component.componentName in base_feature_glyphs_pairs:
                base_feature_glyph_name = base_feature_glyphs_pairs[
                    component.componentName
                ]
                match = re.search(FEATURE_REGEX, base_feature_glyph_name)
                if match is None:
                    continue
                feature = match.group(1)

                feature_glyph_name = joinGlyphName(Font, [glyph.name, feature])
                if Font.glyphs[feature_glyph_name] is None:
                    missing_glyphs.append(feature_glyph_name)

    if len(missing_glyphs) > 0:
        print("Detected %s missing glyphs:" % (len(missing_glyphs)))
        for missing_glyph_name in missing_glyphs:
            print("— %s" % (missing_glyph_name))
    else:
        print("No missing glyphs detected.")


if __name__ == "__main__":
    detect_missing_glyphs()
