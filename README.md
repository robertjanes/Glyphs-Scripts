# Rob’s Glyphs Scripts

#### CleanUpPathsAllGlyphs
Cleans up all the paths in all layers

#### CloseOpenCorners
Closes all open corners in the Font

#### CopyAnchorsFromMasterToMaster
Copies child layers between masters, including masters in different fonts.

#### CopyMasterChildLayersToMaster
Copies anchors between masters. Existing anchors are overwritten.

#### CreateInDesignTaggedText
Creates an inDesign Tagged Text document containing all glyphs in the font.

#### Delete Background Layers
Clears the background layers of the selected layers.

#### Find Bracket and Brace Layers
Logs the names of all bracket and brace layers to the console.

#### HalfAllKerningValues
Halves the values of all kerning pairs in all masters.

#### InstanceInterpolationsReport
View a report displaying each instances interpolation coefficients.

#### SwapGlyphNames
Swaps the names of 2 glyphs. Useful for switching alternative, ssXX glyphs.

#### VariableFontExportWithDecomposeComponents !!!Use at own risk!!!
Exports the font as a variable font with decomposed components.

#### Center Align Anchors
Align all the selected anchors to the center of the layer.

## Running Glyphs Filters in scripts

#### Roughen

```py
RoughenizerFilter = GlyphsApp.NSClassFromString("GlyphsFilterRoughenizer").alloc().init()
RoughenizerFilter.processLayer_withArguments_(layer, [10, 10, 10, 0])
```

## Miscellaneous

#### Change the steps of kern keyboard shortcuts
```py
Glyphs.intDefaults["GSKerningIncrementLow"] = 5
Glyphs.intDefaults["GSKerningIncrementHigh"] = 10
```
