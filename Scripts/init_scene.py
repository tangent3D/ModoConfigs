# python

import modo

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