def joinGlyphName(Font, nameParts):
    fontFeatures = [f.name for f in Font.features]

    def formatNameParts(nameParts):
        newNameParts = []
        for n in range(len(nameParts)):
            namePart = nameParts[n].strip(".")
            namePartSplit = namePart.split(".")
            newNameParts.extend(namePartSplit)
        return newNameParts

    nameParts = formatNameParts(nameParts)
    # Filter out duplicated
    nameParts = list(dict.fromkeys(nameParts))
    _nameParts = list(nameParts)

    def sortNameParts(namePart):
        token = namePart
        if token == "tf":
            token = "tnum"
        if token == "sc":
            token = "c2sc"
        if token in fontFeatures:
            return 100 + fontFeatures.index(token)
        return _nameParts.index(token)

    nameParts.sort(key=sortNameParts)
    return ".".join(nameParts)
