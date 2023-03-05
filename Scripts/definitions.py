# python

import modo

def getProjectName():
	return modo.item.Item('locator.LO').parent.name

def getMESH_LO():
	return modo.item.Item('locator.LO').parent

def getMESH_HI():
	return modo.item.Item('locator.HI').parent

def getMESH_Decals():
	return modo.item.Item('locator.Decals').parent