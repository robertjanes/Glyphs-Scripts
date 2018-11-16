#MenuTitle: Create inDesign Tagged Text
# -*- coding: utf-8 -*-
__doc__="""
Create inDesign Tagged Text
"""
# Author: Robert Janes
# robertjanes.com.au

import GlyphsApp
import os
saveLocation = GlyphsApp.GetFolder()

if saveLocation != None:
	textString = "<ASCII-MAC>\n"
	textString += "<Version:5><FeatureSet:InDesign-Roman><ColorTable:=<Black:COLOR:CMYK:Process:0,0,0,1>>"
	textString += "<DefineParaStyle:FontTableStyle=<Nextstyle:FontTableStyle><cLigatures:0><cFont:" + Font.familyName + "><cOTFContAlt:0>>"
	textString += "<ParaStyle:FontTableStyle>"

	for i, glyph in enumerate(Font.glyphs):
		textString += "<cSpecialGlyph:" + str(i) + "><0xFFFD> <cSpecialGlyph:>"

	f = open(os.path.join(saveLocation, Font.familyName.replace(' ', '') + '-inDesignTaggedText.txt'), "w")
	f.write(textString)
	f.close()
