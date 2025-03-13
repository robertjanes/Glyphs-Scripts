# MenuTitle: Stack Node Onto Node
# -*- coding: utf-8 -*-
__doc__ = """
Stack Node Onto Node
"""

layer = Font.selectedLayers[0]

for path in layer.paths:
    for n, node in reversed(list(enumerate(path.nodes))):
        if node.type == "offcurve":
            continue
        if node in layer.selection:
            newNode = GSNode(node.position)
            if node.smooth and (
                node.nextNode.smooth or node.nextNode.type == "offcurve"
            ):
                newNode.smooth = True
            path.nodes.insert(n + 1, newNode)
