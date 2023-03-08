# python

from definitions import *

def showLow():
	# Don't display deformers
	lx.eval('view3d.enableDeformers false')

	lx.eval('select.type item')
	lx.eval('unhide')
	getMESH_LO().select(replace=True)
	lx.eval('select.itemHierarchy')
	lx.eval('hide.unsel')
	lx.eval('select.vertexMap Texture txuv add')

def showHigh():
	# Don't display deformers
	lx.eval('view3d.enableDeformers false')

	lx.eval('select.type item')
	lx.eval('unhide')
	getMESH_HI().select(replace=True)
	lx.eval('select.itemHierarchy')
	lx.eval('deformer.selectBaseMesh')
	lx.eval('hide.unsel')

def showHighDeformers():
	# Show deformers
	lx.eval('view3d.enableDeformers true')

	lx.eval('select.type item')
	lx.eval('unhide')
	getMESH_HI().select(replace=True)
	lx.eval('select.itemHierarchy')
	lx.eval('hide.unsel')

def showHighLow():
	# Don't display deformers
	lx.eval('view3d.enableDeformers false')

	lx.eval('select.type item')
	lx.eval('unhide')
	getMESH_HI().select(replace=True)
	getMESH_LO().select()
	lx.eval('select.itemHierarchy')
	lx.eval('deformer.selectBaseMesh')
	lx.eval('hide.unsel')

def showDecals():
	# Don't display deformers
	lx.eval('view3d.enableDeformers false')

	lx.eval('select.type item')
	lx.eval('unhide')
	getMESH_Decals().select(replace=True)
	lx.eval('select.itemHierarchy')
	lx.eval('hide.unsel')

def showHighDecals():
	# Don't display deformers
	lx.eval('view3d.enableDeformers false')

	lx.eval('select.type item')
	lx.eval('unhide')
	getMESH_HI().select(replace=True)
	getMESH_Decals().select()
	lx.eval('select.itemHierarchy')
	lx.eval('deformer.selectBaseMesh')
	lx.eval('hide.unsel')
	getMESH_Decals().select()

def showAll():
	# Don't display deformers
	lx.eval('view3d.enableDeformers false')

	lx.eval('select.type item')
	lx.eval('unhide')
	getMESH_HI().select(replace=True)
	getMESH_Decals().select()
	getMESH_LO().select()
	lx.eval('select.itemHierarchy')
	lx.eval('deformer.selectBaseMesh')
	lx.eval('hide.unsel')

# Redefine user value if undefined or if specified

if lx.arg() == 'lo':
	showLow()

if lx.arg() == 'hi':
	showHigh()

if lx.arg() == 'hidef':
	showHighDeformers()

if lx.arg() == 'hilo':
	showHighLow()

if lx.arg() == 'dec':
	showDecals()

if lx.arg() == 'hidec':
	showHighDecals()

if lx.arg() == 'all':
	showAll()