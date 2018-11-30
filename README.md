# Rob’s Glyphs Scripts

#### CopyAnchorsFromMasterToMaster
Copies child layers between masters, including masters in different fonts.

#### CopyMasterChildLayersToMaster
Copies anchors between masters. Existing anchors are overwritten.

#### CreateInDesignTaggedText
Creates an inDesign Tagged Text document containing all glyphs in the font.

#### Delete Background Layers
Clears the background layers of the selected layers.

#### HalfAllKerningValues
Halves the values of all kerning pairs in all masters.

#### SwapGlyphNames
Swaps the names of 2 glyphs. Useful for switching alternative, ssXX glyphs.

#### VariableFontExportWithDecomposeComponents !!!Use at own risk!!!
Exports the font as a variable font with decomposed components.

## Running Glyphs Filters in scripts

#### Roughen

```py
RoughenizerFilter = GlyphsApp.NSClassFromString("GlyphsFilterRoughenizer").alloc().init()
RoughenizerFilter.processLayer_withArguments_(layer, [10, 10, 10, 0])
```
