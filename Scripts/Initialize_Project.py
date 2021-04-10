# python

import modo

# Roughly check if the scene has already been initialized
# FIXME: Should exit gracefully
scene = modo.Scene()

try:
	mesh = scene.item('locator.LO')
	modo.dialogs.alert('Scene already initialized', 'Please create a new scene first.', dtype='info')
except:
	pass

# Create a new mesh container (Mesh_Decals)
lx.eval('layer.new')
lx.eval('tool.set prim.cube on 0')
lx.eval('tool.reset prim.cube')
lx.eval('tool.apply')
lx.eval('tool.set prim.cube off 0')
lx.eval('item.name Mesh_Decals')
MESH_Decals = modo.item.Item(item=None)

# Create a new mesh container (MESH_HI)
lx.eval('layer.new')
lx.eval('tool.set prim.cube on 0')
lx.eval('tool.reset prim.cube')
lx.eval('tool.apply')
lx.eval('tool.set prim.cube off 0')
lx.eval('item.name Mesh_HI')
MESH_HI = modo.item.Item(item=None)

# Create a new mesh container (Mesh_LO)
lx.eval('layer.new')
lx.eval('tool.set prim.cube on 0')
lx.eval('tool.reset prim.cube')
lx.eval('tool.apply')
lx.eval('tool.set prim.cube off 0')
lx.eval('item.name Mesh_LO')
MESH_LO = modo.item.Item(item=None)

### Create RoundEdge material and assign to MESH_HI
MESH_HI.select(replace=True)
lx.eval('poly.setMaterial RoundEdge {0.8 0.8 0.8} 1.0 0.04 true false')
MESH_HI.deselect()
# Define RoundEdge material properties
lx.eval('item.channel advancedMaterial$smAngle 25.0')
lx.eval('item.channel advancedMaterial$rndAngle 25.0')
lx.eval('item.channel advancedMaterial$rndWidth 0.01')
lx.eval('item.channel advancedMaterial$rndSame true')

### Cleaning up the default scene ###

# Delete default mesh
modo.item.Item('Mesh').select(replace=True)
lx.eval('delete')

# # Delete default Final Color Output
modo.item.Item('Final Color Output').select(replace=True)
lx.eval('delete')

# # Delete default Alpha Output
modo.item.Item('Alpha Output').select(replace=True)
lx.eval('delete')

### Creating Render Outputs ###

# Create the Alpha Render Output
lx.eval('shader.create renderOutput')
lx.eval('shader.setEffect shade.alpha')
RO_Alpha = modo.item.Item(item=None)

# Create the Diffuse Color Render Output
lx.eval('shader.create renderOutput')
lx.eval('shader.setEffect mat.diffCol')
RO_Diffuse = modo.item.Item(item=None)

# Create the Shading Normal Render Output
lx.eval('shader.create renderOutput')
lx.eval('shader.setEffect shade.normal')
lx.eval('item.channel renderOutput$remap true')
RO_ShadingNormal = modo.item.Item(item=None)

# Create the Surface ID Render Output
lx.eval('shader.create renderOutput')
lx.eval('shader.setEffect geo.surface')
RO_ID = modo.item.Item(item=None)

### Creating texture layers ###

# Create Texture Layer Occlusion (Curvature) 
lx.eval('shader.create occlusion')
lx.eval('item.name Curvature occlusion')
lx.eval('item.channel occlusion$type curvature')
lx.eval('item.channel occlusion$rays 1')
lx.eval('item.channel occlusion$dist 0.1')
#lx.eval('item.channel occlusion$sameSurf true')
TEX_Curvature = modo.item.Item(item=None)

# Create Texture Layer Wireframe Texture
lx.eval('shader.create val.wireframe')
lx.eval('item.channel val.wireframe$edgeMap Seams')
lx.eval('item.channel val.wireframe$transWidth 1.0')
TEX_Wireframe = modo.item.Item(item=None)

# Create Wireframe Texture instance "Wireframe Bump"
lx.eval('texture.instance')
lx.eval('shader.setEffect bump')
lx.eval('item.channel textureLayer$invert true')
lx.eval('item.name "Wireframe Bump"')

### Create "LO" material and assign to MESH_LO
MESH_LO.select(replace=True)
lx.eval('poly.setMaterial Mesh {1.0 1.0 1.0} 1.0 0.04 true false false')
MESH_LO.deselect()
MAT_LO = modo.item.Item(item=None)
# Set smoothing angle to 25 degrees
lx.eval('item.channel advancedMaterial$smAngle 25.0')
MAT_LO.deselect()
MASK_MAT_LO = modo.item.Item(item=None)

# Create "Decals" material and assign to MESH_Decals
# Create here to ensure it is at the top of the shader tree
MESH_Decals.select(replace=True)
lx.eval('poly.setMaterial Decals {0.0 0.0 0.0} 1.0 0.04 true false false')

### Creating Bake Items ###

# Create World Space Normals Render Output Bake Item
lx.eval('bakeItem.createOutputBake')
lx.eval('item.name "World Space Normals Bake"bakeItemRO')
lx.eval('bakeItem.renderOutput '+RO_ShadingNormal.id+'')
BAKE_RO_ShadingNormal = modo.item.Item(item=None)

# Create Curvature (Diffuse Color) Render Output Bake Item
lx.eval('bakeItem.createOutputBake')
lx.eval('item.name "Curvature Bake"bakeItemRO')
lx.eval('bakeItem.renderOutput '+RO_Diffuse.id+'')
BAKE_RO_Curvature = modo.item.Item(item=None)

# Create Alpha Mask Bake Item
lx.eval('bakeItem.createOutputBake')
lx.eval('item.name "Alpha Mask Bake"bakeItemRO')
lx.eval('bakeItem.renderOutput '+RO_Alpha.id+'')
BAKE_RO_Alpha = modo.item.Item(item=None)

# Create Surface ID Bake Item
lx.eval('bakeItem.createOutputBake')
lx.eval('item.name "Surface ID Bake"bakeItemRO')
lx.eval('bakeItem.renderOutput '+RO_ID.id+'')
BAKE_RO_ID = modo.item.Item(item=None)

# Create Decals ID Bake Item
lx.eval('bakeItem.createOutputBake')
lx.eval('item.name "Decals ID Bake"bakeItemRO')
lx.eval('bakeItem.renderOutput '+RO_ID.id+'')
BAKE_RO_Decals = modo.item.Item(item=None)

### Creating Texture Bake Items ###

# Create Tangent Space Normals Texture Bake Item
lx.eval('bakeItem.createTextureBake')
lx.eval('item.name "Tangent Space Normals Texture Bake"bakeItemTexture')
lx.eval('item.channel bakeItemTexture$useNormalPreset true')
BAKE_TEX_Normal = modo.item.Item(item=None)

### Configuring common bake settings on Bake Items ###

BAKE_RO_ShadingNormal.select(replace=True)
BAKE_RO_Curvature.select()
BAKE_RO_Alpha.select()
BAKE_RO_ID.select()
BAKE_RO_Decals.select()
lx.eval('item.channel bakeItemRO$bakeFrom true')
lx.eval('item.channel bakeItemRO$hiddenTarget true')
lx.eval('item.channel bakeItemRO$hiddenSource true')
lx.eval('item.channel bakeItemRO$hiddenOutput true')
lx.eval('item.channel bakeItemRO$saveOutputFile true')
lx.eval('item.channel bakeItemRO$distance 0.005')
lx.eval('item.channel bakeItemRO$width 512')
lx.eval('item.channel bakeItemRO$height 512')
lx.eval('bakeItem.setUV Texture')

BAKE_TEX_Normal.select(replace=True)
lx.eval('item.channel bakeItemTexture$bakeFrom true')
lx.eval('item.channel bakeItemTexture$hiddenTarget true')
lx.eval('item.channel bakeItemTexture$hiddenSource true')
lx.eval('item.channel bakeItemTexture$hiddenOutput true')
lx.eval('item.channel bakeItemTexture$saveOutputFile true')
lx.eval('item.channel bakeItemTexture$distance 0.005')

# Hide non-essential items
lx.eval('shader.setVisible '+RO_ID.id+' false')
lx.eval('shader.setVisible '+RO_ShadingNormal.id+' false')
lx.eval('shader.setVisible '+RO_Alpha.id+' false')

### Project organization ###

# Get project name from user
lx.eval("user.defNew name:UserValueProjectName type:string life:momentary")
lx.eval('user.def UserValueProjectName dialogname "Set project name"')
lx.eval("user.def UserValueProjectName username {Name}")

try:
    lx.eval("?user.value UserValueProjectName")
    userResponse = lx.eval("dialog.result ?")
    
except:
    userResponse = lx.eval("dialog.result ?")
    sys.exit()
    
projectName = lx.eval("user.value UserValueProjectName ?")

lx.out('Project name:',projectName)

# Rename Mesh_LO to match project name
MESH_LO.select(replace=True)
lx.eval('item.name "' + projectName + '"')

# Rename MESH_HI to match project name
MESH_HI.select(replace=True)
lx.eval('item.name "' + projectName + '_HI"')

# Rename MESH_Decals to match project name
MESH_Decals.select(replace=True)
lx.eval('item.name "' + projectName + '_Decals"')

# Rename mesh material to match project name
MASK_MAT_LO.select(replace=True)
lx.eval("dialog.result ok")
lx.eval('texture.name "' + projectName + '"')

# Rename render output file names with project name + suffix
BAKE_RO_ShadingNormal.select(replace=True)
lx.eval('item.channel bakeItemRO$outPattern "' + projectName +'_World_Space_Normals"')

BAKE_RO_Curvature.select(replace=True)
lx.eval('item.channel bakeItemRO$outPattern "' + projectName +'_Curvature"')

BAKE_RO_ID.select(replace=True)
lx.eval('item.channel bakeItemRO$outPattern "' + projectName +'_ID"')

BAKE_RO_Alpha.select(replace=True)
lx.eval('item.channel bakeItemRO$outPattern "' + projectName +'_Mask"')

BAKE_RO_Decals.select(replace=True)
lx.eval('item.channel bakeItemRO$outPattern "' + projectName +'_Decals_ID"')

# Set render output directory (usually project's 'bake' folder)
lx.eval('dialog.setup dir')
lx.eval('dialog.title "Set project bake directory"')
lx.eval('dialog.result "D:\Dropbox"')
lx.eval('dialog.open')
output_dir = lx.eval('dialog.result ?')

# Set output directory on Render Output Bake Items
BAKE_RO_Alpha.select(replace=True)
BAKE_RO_Curvature.select()
BAKE_RO_ID.select()
BAKE_RO_ShadingNormal.select()
BAKE_RO_Decals.select()
lx.eval('item.channel outLocation "' + output_dir + '"')

# Creating normal maps and configuring the project for UDIMs

def askUDIMs():
	# Check if the project should be configured for UDIMs
	return modo.dialogs.yesNo('UDIMs','Use UDIMs?')

def askRangeStart():
	#Get desired UDIM range start from user
	lx.eval("user.defNew name:UserValueRangeStart type:string life:momentary")
	lx.eval('user.def UserValueRangeStart dialogname "Set UDIM Range Start"')
	lx.eval("user.def UserValueRangeStart username {Default: 1001}")

	try:
		lx.eval("?user.value UserValueRangeStart")
		userResponse = lx.eval("dialog.result ?")
	except:
		pass

	rangeStart = lx.eval("user.value UserValueRangeStart ?")

	if rangeStart == "":
		rangeStart = "1001"

	return rangeStart

def askRangeEnd():
	#Get desired UDIM range end from user
	lx.eval("user.defNew name:UserValueRangeEnd type:string life:momentary")
	lx.eval('user.def UserValueRangeEnd dialogname "Set UDIM Range End"')
	lx.eval("user.def UserValueRangeEnd username {Default: 1001}")

	try:
		lx.eval("?user.value UserValueRangeEnd")
		userResponse = lx.eval("dialog.result ?")
	except:
		pass

	rangeEnd = lx.eval("user.value UserValueRangeEnd ?")

	if rangeEnd == "":
		rangeEnd = "1001"

	return rangeEnd

def createNormalsUDIMs():
	MASK_MAT_LO.select(replace=True)
	lx.eval('clip.udimWizard "'+output_dir+'" '+projectName+'_Normal_Base '+rangeStart+' '+rangeEnd+' x2048 rgb false false format:PNG overwrite:false')
	lx.eval('shader.create imageMap 0')
	# Set TS Normal image map folder effect to Normal while it's selected
	lx.eval('shader.setEffect normal')

def createNormalsDefault():
	# Make a normal map image and parent it in the MESH_LO material
	lx.eval('clip.newStill "' + output_dir + '\\' + projectName + '_Normal_Base.png" x2048 RGB false false {0.0 0.0 0.0} PNG (none)')
	lx.eval('select.subItem {' + projectName + '_Normal_Base:videoStill001} set mediaClip')
	lx.eval('texture.new clip:{' + projectName +'_Normal_Base:videoStill001}')
	MASK_MAT_LO.select()
	lx.eval('texture.parent '+MASK_MAT_LO.id+'')
	lx.eval('select.subItem '+MASK_MAT_LO.id+' remove')
	lx.eval('item.channel textureLayer(txtrLocator)$projType uv')
	lx.eval('texture.setUV Texture')
	lx.eval('shader.setEffect normal')
	# While texture layer is selected, assign normal texture output to TS normal bake item
	BAKE_TEX_Normal.select()
	lx.eval('bakeItem.texture {}')
	lx.eval('bakeItem.setAsTextureOutput 0')
	lx.eval('select.drop item')
	pass

def setBakeUDIMs():
	BAKE_RO_Alpha.select(replace=True)
	BAKE_RO_Curvature.select()
	BAKE_RO_ID.select()
	BAKE_RO_ShadingNormal.select()
	BAKE_RO_Decals.select()
	lx.eval('item.channel bakeItemRO$useUDIM true')
	lx.eval('item.channel bakeItemRO$startUDIM '+rangeStart+'')
	lx.eval('item.channel bakeItemRO$endUDIM '+rangeEnd+'')

if askUDIMs() == "yes":
	rangeStart = askRangeStart()
	rangeEnd = askRangeEnd()
	createNormalsUDIMs()
	setBakeUDIMs()
else:
	createNormalsDefault()	

# Delete MESH_HI and MESH_Decals UV maps
MESH_HI.select(replace=True)
MESH_Decals.select()
lx.eval('select.vertexMap Texture txuv replace')
lx.eval('vertMap.delete txuv')

# Set render frame to 1:1 ratio
lx.eval('render.res 0 1024')
lx.eval('render.res 1 1024')

# Create locators so other scripts can identify the meshes in the scene
lx.eval('item.create locator')
lx.eval('item.name locator.HI locator')
locHI = modo.item.Item(item=None)
lx.eval('item.parent '+locHI.id+' '+MESH_HI.id+'')

lx.eval('item.create locator')
lx.eval('item.name locator.LO locator')
locLO = modo.item.Item(item=None)
lx.eval('item.parent '+locLO.id+' '+MESH_LO.id+'')

lx.eval('item.create locator')
lx.eval('item.name locator.Decals locator')
locDecals = modo.item.Item(item=None)
lx.eval('item.parent '+locDecals.id+' '+MESH_Decals.id+'')

# Lock the mesh containers
MESH_HI.select(replace=True)
MESH_LO.select()
MESH_Decals.select()
lx.eval('item.channel locator$lock on')

lx.eval('select.drop item')

# Make MESH_HI the only item visible in the scene
lx.eval('@show_HI.py')

# Assign bake item sources/targets
lx.eval('@set_sources_targets.py')