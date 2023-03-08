# python

# Project exporter

# When user value exportSeparate is set, all child meshes are exported as separate files.
# When user value exportMerge is set, all child meshes are merged and exported as separate files.
#	If exportSeparate is also set, submeshes in child meshes are merged if present and exported as separate files.
# When user value exportNoMaterials is set, parent mesh iterations are separately exported without materials.
# When user value exportCollada is set, all exported meshes are converted to Collada (.DAE). Requires MeshSmith.

from definitions import *
import os
scene = modo.Scene()

import traceback

def main():
	# Ensure all mesh locators are present before proceeding
	ensureLocators()

	# Create user value for output directory if none exists
	if not lx.eval('query scriptsysservice userValue.isDefined ? output_dir'):
		lx.eval('user.defNew name:output_dir life:temporary')

	# Prompt for output directory if undefined
	if lx.eval('user.value output_dir ?') == "":
		promptNewDir()

	# Parse arguments
	args = lx.args()
	for arg in args:
		# Change export directory and exit if argument supplied
		if arg == 'new':
			promptNewDir()
			sys.exit(0)

	# Store user's FBX export settings
	fbx_export_setting = lx.eval1('user.value sceneio.fbx.save.exportType ?')
	fbx_units_setting = lx.eval1('user.value sceneio.fbx.save.units ?')
	fbx_materials_setting = lx.eval1('user.value sceneio.fbx.save.materials ?')

	# Set FBX export setting to 'export selection with hierarchy'
	lx.eval('user.value sceneio.fbx.save.exportType FBXExportSelectionWithHierarchy')
	# Set FBX export units to 'm'
	lx.eval('user.value sceneio.fbx.save.units m')
	# Set FBX export materials to 'true'
	lx.eval('user.value sceneio.fbx.save.materials true')

	# Export low poly
	process(getMESH_LO(), \
		lx.eval('user.value exportSeparate ?'), \
		lx.eval('user.value exportMerge ?'), \
		lx.eval('user.value exportNoMaterials ?'), \
		lx.eval('user.value exportCollada ?'))

	# Export high poly
	process(getMESH_HI(), False, False, False, False)

	# Export decals
	process(getMESH_Decals(), False, False, False, False)

	# Restore user's FBX export settings
	lx.eval('user.value sceneio.fbx.save.exportType {}'.format(fbx_export_setting))
	lx.eval('user.value sceneio.fbx.save.units {}'.format(fbx_units_setting))
	lx.eval('user.value sceneio.fbx.save.materials {}'.format(fbx_materials_setting))

# === FUNCTION DEFINITIONS ===

# Process and export selection according to parameters
def process(source, boolSeparate, boolMerge, boolNoMaterials, boolCollada):
	# Duplicate hiearchy to new item
	nameSource = source.name
	source.select(replace=True)
	lx.eval('item.duplicate false locator true true')
	# Store duplicate parent and direct descendants
	parent = modo.item.Item(item=None)
	children = lx.evalN('query layerservice layer.children ? main')

	# Freeze all geometry, normals, etc.
	lx.eval('select.itemHierarchy')
	freeze()

	# Export all children and hierarchy (excludes child locator)
	for child in children:
		# Add mesh item to selection
		lx.eval('select.subItem {} add mesh'.format(child))
	export(nameSource, boolNoMaterials, boolCollada)

	# Export children as separate files if specified
	if boolSeparate == True:
		# Process on every child mesh item
		for child in children:
			# Replace selection with child mesh item
			lx.eval('select.subItem {} set mesh'.format(child))
			# Move mesh item to origin
			lx.eval ('transform.channel pos.X 0.0')
			lx.eval ('transform.channel pos.Y 0.0')
			lx.eval ('transform.channel pos.Z 0.0')
			# Get mesh item name from child mesh item
			# Warning: strips 4 characters from end to account for ' (n)' suffix on duplicate items!
			nameMesh = lx.eval('query layerservice layer.name ? {}'.format(child))[:-4]
			# Don't bother exporting child meshes with no materials for now
			export(nameMesh, False, boolCollada)
			# Merge all submeshes of children, if present, and export merged meshes if specified
			if boolMerge == True:
				for child in children:
					# Replace selection with child mesh item
					lx.eval('select.subItem {} set mesh'.format(child))
					# Proceed if submeshes present
					if (lx.eval('query layerservice layer.childCount ? {}'.format(child))) > 0:
						nameMesh = lx.eval('query layerservice layer.name ? {}'.format(child))[:-4]
						lx.eval('select.itemHierarchy')
						lx.eval('layer.mergeMeshes true')
						lx.eval('item.name {} mesh'.format(nameMesh))
						# Again, don't bother exporting merged submeshes with no materials for now
						export('{}_Merged'.format(nameMesh), False, boolCollada)

	# Export merged hierarchy
	if boolMerge == True:
	# Select all child mesh items
		lx.eval('select.drop item')
		for child in children:
			lx.eval('select.subItem {} add mesh'.format(child))
		# Merge meshes
		lx.eval('layer.mergeMeshes true')
		# Rename merged mesh to name of former parent
		lx.eval('item.name {} mesh'.format(nameSource))
		# Export merged mesh
		export('{}_Merged'.format(nameSource), boolNoMaterials, boolCollada)

	# Clean up duplicate mesh items
	delete(parent)

# Export selection and convert to Collada if specified
def export(nameBase, boolNoMaterials, boolCollada):
	# Store ID of mesh item to be exported
	mesh = lx.eval('query layerservice layer.name ?')

	# Export mesh item with hierarchy
	path = os.path.join (lx.eval('user.value output_dir ?'), nameBase)
	lx.eval('!scene.saveAs "{}" fbx true'.format(path))

	# Export without materials as separate file if specified
	if boolNoMaterials == True:
		# Reselect original mesh item to be exported
		modo.item.Item(mesh).select(replace=True)
		#lx.eval('select.subItem {} set mesh'.format(mesh))
		# Disable exporting FBX materials
		lx.eval('user.value sceneio.fbx.save.materials false')
		path = os.path.join (lx.eval('user.value output_dir ?'), '{}_NoMats'.format(nameBase))
		lx.eval('!scene.saveAs "{}" fbx true'.format(path))
		# Reenable exporting FBX materials
		lx.eval('user.value sceneio.fbx.save.materials true')

	# Convert exported FBX to Collada if specified
	if boolCollada == True:
		os.popen("MeshSmith -i {0}.fbx -o {0}.dae -f collada".format(path))

	lx.eval('select.drop item')

# Freeze subdivision, Mesh Operations ... 
def freeze():
	# Freeze deformers
	lx.eval('deformer.freeze false')

	# Freeze geometry
	lx.eval('poly.freeze face false 2 true true true true 5.0 false Morph')

	# Freeze vertex normals if vertex map is not present
	try:
		lx.eval('select.vertexMap "Vertex Normal" norm add')
	except RuntimeError:
		lx.eval('vertMap.normals "Vertex Normal" true 1.0 Texture false')

	lx.eval('select.drop item')

# Clean up duplicate mesh
def delete(item):
	modo.scene.Scene(scene=scene.scene)
	item.select(replace=True)
	lx.eval('delete')

# Ensure all mesh locators exist or exit
def ensureLocators():
	try:
		getMESH_LO()
		getMESH_HI()
		getMESH_Decals()
	except:
		modo.dialogs.alert('Error', 'One or more locator items not found.', dtype='error')
		sys.exit(1)

def promptNewDir():
	newDir = modo.dialogs.dirBrowse('Mesh export path', 'D:\\Dropbox\\Projects')
	
	# Abort execution if aborted by user
	if newDir is None:
		sys.exit(2)
	else:
		lx.eval('user.value output_dir ' + '"' + newDir + '"')

if __name__ == '__main__':
   try:
      main()
   except:
      lx.out(traceback.format_exc())