# python

from definitions import *
import os
scene = modo.Scene()

# Fetch and return user value content
def dirValue():
	return lx.eval('user.value output_dir ?')

def dirDefined():
	return lx.eval('query scriptsysservice userValue.isDefined ? output_dir')

def newDir():
	newPath = modo.dialogs.dirBrowse('Mesh export path', 'D:\\Dropbox\\Projects')
	
	if newPath is None:
		sys.exit(2)
	else:
		lx.eval('user.value output_dir ' + '"' + newPath + '"')

def exportFBX(baseName):
	path = os.path.join (dirValue(), baseName + '.fbx')

	# Export to FBX
	lx.eval ('!scene.saveAs "%s" fbx true' % path)

# Freeze subdivision, Mesh Operations ... 
def freeze():
	# Freeze deformers
	lx.eval('deformer.freeze false')

	# Freeze geometry
	lx.eval('poly.freeze face false 2 true true true true 5.0 false Morph')

	# Freeze vertex normals
	lx.eval('vertMap.normals "Vertex Normal" true 1.0 Texture false')

# Remove duplicate/merged mesh
def removeDuplicate(item):
	modo.scene.Scene(scene=scene.scene)
	item.select(replace=True)
	lx.eval('delete')

# Export low poly mesh and merged low poly mesh
def exportLow():
	getMESH_LO().select(replace=True)
	lx.eval('select.itemHierarchy')

	# Deselect locator
	modo.item.Item('locator.LO').deselect()

	# Duplicate to new item
	lx.eval('item.duplicate false locator false true')	

	freeze()

	duplicate = modo.item.Item(item=None)

	# Export hierarchy
	exportFBX('%s_LO' % getProjectName())

	# Merge meshes
	modo.scene.Scene(scene=scene.scene)
	duplicate.select(replace=True)
	lx.eval('select.itemHierarchy')
	lx.eval('layer.mergeMeshes true')

	# Export merged mesh
	exportFBX('%s_LO_Merged' % getProjectName())

	removeDuplicate(duplicate)

def exportHigh():
	getMESH_HI().select(replace=True)
	lx.eval('select.itemHierarchy')

	# Deselect locator
	modo.item.Item('locator.HI').deselect()

	# Duplicate to new item
	lx.eval('item.duplicate false locator false true')

	freeze()

	duplicate = modo.item.Item(item=None)

	# Export mesh
	exportFBX('%s_HI' % getProjectName())	

	removeDuplicate(duplicate)

def exportDecals():
	getMESH_Decals().select(replace=True)
	lx.eval('select.itemHierarchy')

	# Deselect locator
	modo.item.Item('locator.Decals').deselect()

	# Duplicate to new item
	lx.eval('item.duplicate false locator false true')	

	freeze()

	duplicate = modo.item.Item(item=None)

	# Export hierarchy
	exportFBX('%s_Decals' % getProjectName())

	removeDuplicate(duplicate)

# Start of script

# Ensure all mesh locators exist
try:
	getMESH_LO()
	getMESH_HI()
	getMESH_Decals()
except:
	modo.dialogs.alert('Error', 'One or more locator items not found.', dtype='error')
	sys.exit(1)

# Create user value if none exists
if not dirDefined():
	lx.eval('user.defNew name:output_dir life:temporary')

# Redefine user value if undefined or if specified
if dirValue() == "" or lx.arg() == 'new':
	newDir()

# Print defined export path to log
print('Mesh export path: ' + dirValue())

# Export all project meshes
exportLow()
exportHigh()
exportDecals()