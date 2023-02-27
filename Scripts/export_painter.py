# python

import os
import glob
from definitions import *

# Get project name from LO mesh
name = getProjectName()

# Get bake item output directory
output_dir = getOutputDir()

# Check if project is using UDIM workflow
if (getBAKE_RO_ShadingNormal().channel('useUDIM').get() == 1):
	# Get UDIM range
	endUDIM = int(getBAKE_RO_ShadingNormal().channel('endUDIM').get())
	useUDIM = 'true'
else:
	useUDIM = 'false'

# File base names
base = output_dir + '/'
mesh = base + name + '.fbx'
wsSuffix = '_World_Space_Normals'
tsSuffix = '_Normal_Base'
# aoSuffix = '_Ambient_Occlusion'
idSuffix = '_ID'
cuSuffix = '_Curvature'
deSuffix = '_Decals_ID'
seSuffix = '_Seams'

ws = base + name + wsSuffix
ts = base + name + tsSuffix
# ao = base + name + aoSuffix
id = base + name + idSuffix
cu = base + name + cuSuffix
de = base + name + deSuffix
se = base + name + seSuffix

cmdPainter = 'start /B nircmd exec max "Adobe Substance 3D Painter" '
cmdXNormal = 'xnormal '

# Delete a file path if it exists
def delExistent(dest):
	if (os.path.exists (dest)):
		os.remove(dest)

# Rename UDIM bakes for compatibility with Substance Painter legacy UV Tile workflow
# Only renames if files exist to support re-baking bake items
def renameUDIM():
	if (useUDIM == 'true'):
		for i in range(1001, int(endUDIM+1), 1):
			src = ws + '_' + str(i) + '.png'
			if (os.path.exists (src)):
				dest = base + str(i) + wsSuffix + '.png'
				delExistent(dest)
				os.rename(src, dest)

			src = ts + '_' + str(i) + '.tiff'
			if (os.path.exists (src)):
				dest = base + str(i) + tsSuffix + '.tiff'
				delExistent(dest)
				os.rename(src, dest)

			# src = ao + '_' + str(i) + '.png'
			# if (os.path.exists (src)):
			# 	dest = base + str(i) + aoSuffix + '.png'
			# 	delExistent(dest)
			# 	os.rename(src, dest)

			src = id + '_' + str(i) + '.png'
			if (os.path.exists (src)):
				dest = base + str(i) + idSuffix + '.png'
				delExistent(dest)
				os.rename(src, dest)

			src = cu + '_' + str(i) + '.png'
			if (os.path.exists (src)):
				dest = base + str(i) + cuSuffix + '.png'
				delExistent(dest)
				os.rename(src, dest)

			src = de + '_' + str(i) + '.png'
			if (os.path.exists (src)):
				dest = base + str(i) + deSuffix + '.png'
				delExistent(dest)
				os.rename(src, dest)

			src = se + '_' + str(i) + '.png'
			if (os.path.exists (src)):
				dest = base + str(i) + seSuffix + '.png'
				delExistent(dest)
				os.rename(src, dest)

def open():
	if (useUDIM == 'true'):
		# Rename bakes for legacy UV Tile workflow
		renameUDIM()
		meshMapList = ""
		for i in range(1001, int(endUDIM+1), 1):
			meshMapList = (meshMapList +
				' --mesh-map ' + base + str(i) + '_World_Space_Normals.png' + 
				' --mesh-map ' + base + str(i) + '_Normal_Base.tiff' +
				# ' --mesh-map ' + base + str(i) + '_Ambient_Occlusion.png' +
				' --mesh-map ' + base + str(i) + '_ID.png' +
				' --mesh-map ' + base + str(i) + '_Curvature.png' +
				' --mesh-map ' + base + str(i) + '_Decals_ID.png' +
				' --mesh-map ' + base + str(i) + '_Seams.png')
		os.popen(cmdPainter + '--mesh ' + mesh + ' ' + '--split-by-udim' + meshMapList)
	else:
		meshMapList = (
			' --mesh-map ' + ts + '.tiff' + # TS Normal Map
			' --mesh-map ' + ws + '.png' +  # WS Normal Map
			# ' --mesh-map ' + ao + '.png' +  # Ambient Occlusion
			' --mesh-map ' + id + '.png' +  # Surface ID Map
			' --mesh-map ' + cu + '.png' +  # Curvature Map
			' --mesh-map ' + de + '.png' +  # Decals ID Map
			' --mesh-map ' + se + '.png')   # Seams Mask
		os.popen(cmdPainter + '--mesh ' + mesh + meshMapList)
		
def bake():
	# Reduce bake item resolution if argument supplied
	if (lx.arg() == 'draft'):
		bakeArg = 'draft'
	else:
		bakeArg = ''
	lx.eval('@bake_all.py ' + bakeArg)

# Export LO meshes
def exportMesh():
	# Freeze vertex normals before anything
	lx.eval('@set_UV_hard_edges_weighted.py')
	lx.eval('@set_vertex_normals.py')

	# Export separate meshes (1001.fbx, 1002.fbx ... ) for each UDIM for XNormal OS/TS normal map conversion.
	# Expects that each UDIM have materials named 1001, 1002, etc!
	if (useUDIM == 'true'):
		for i in range(1001, int(endUDIM+1), 1):
			getMESH_LO().select(replace=True)
			lx.eval('select.itemHierarchy')
			modo.item.Item(str(i) + ' (Material)').select()
			lx.eval('select.vertexMap Texture txuv add')
			# Select material polygons
			lx.eval('material.selectPolygons')
			# Duplicate UDIM polygons to a new item
			lx.eval('copy')
			lx.eval('layer.new')
			lx.eval('paste')
			# Move UV to 1001 based on its UDIM 
			lx.eval('tool.set TransformMove on')
			lx.eval('tool.viewType uv')
			lx.eval('tool.xfrmDisco true')
			lx.eval('tool.attr xfrm.transform U -' + str(i - 1001))
			lx.eval('tool.doApply')
			# Export UDIM as separate mesh
			lx.eval('select.typeFrom item')
			lx.eval('scene.saveAs "' + output_dir + '/' + str(i) + '.fbx" fbx true')
			lx.eval('delete')

	# Export LO mesh and hierarchy to bake item output directory
	getMESH_LO().select(True)
	lx.eval('scene.saveAs "' + output_dir + '/' + name + '.fbx" fbx true')

# Convert object space normal map to tangent space normal map
# xNormal directory must be in PATH
def os2ts():
	if (useUDIM == 'true'):
		for i in range(1001, int(endUDIM+1), 1):
			if (os.path.exists (ws + '_' + str(i) + '.png')):
				os.popen(cmdXNormal + '-os2ts ' + base + str(i) + '.fbx ' + 'false ' + ws + '_' + str(i) + '.png ' + ts + '_' + str(i) + '.tiff true 16')
	else:
		if (os.path.exists (ws + '.png')):
			os.popen(cmdXNormal + '-os2ts ' + base + name + '.fbx ' + 'false ' + ws + '.png ' + ts + '.tiff true 16')
	
def main():
	# Export LO mesh
	exportMesh()

	# Optionally skip bakes and just open in Substance Painter
	if (lx.arg() == 'open'):
		renameUDIM()
		open()
		exit()

	# Optionally skip bakes and just convert normal maps
	if (lx.arg() == 'os2ts'):
		os2ts()
		renameUDIM()
		exit()
	
	bake()	# Bake all bake items
	os2ts() # Convert OS to TS normal map(s) with XNormal
	open()  # Open output in Substance Painter
			
main()