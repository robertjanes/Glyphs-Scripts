#!/usr/bin/env python
# -*- coding: utf-8 -*-
#MenuTitle: Instance Interpolations Report
__doc__="""
Instance Interpolations Report
"""
from vanilla import Window, TextEditor

text = ""
for instance in Font.instances:
	if instance.active is False: continue
	text += "%s Instance is interpolated with:\n" % (instance.name)
	for instanceInterpolation in instance.instanceInterpolations:
		text += u"• %s: %s Master\n" % ("{0:.2f}".format(instance.instanceInterpolations[instanceInterpolation]), Font.masters[instanceInterpolation].name)
	text += "\n"

class InstanceInterpolationsReport(object):

    def __init__(self):
        self.w = Window((350, 600),
						"Instance Interpolations Report",
						minSize=(300, 450))
        self.w.textEditor = TextEditor((10, 10, -10, -10),
                            text=text,
                            readOnly=True)
        self.w.open()

InstanceInterpolationsReport()
