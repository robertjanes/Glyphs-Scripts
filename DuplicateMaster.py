def duplicateMaster(master):
	newMaster = master.copy()
	Font.masters.append(newMaster)

	# Kerning is seperate from the master and needs to be manually duplicated
	newKerning = Font.kerning[master.id].copy()
	Font.kerning[newMaster.id] = newKerning

	for glyph in Font.glyphs:
		newLayer = glyph.layers[master.id].copy()
		newLayer.associatedMasterId = newMaster.id
		newLayer.layerId = newMaster.id
		# Replace the auto-generated layer with our duplicated one
		glyph.layers[newMaster.id] = newLayer
