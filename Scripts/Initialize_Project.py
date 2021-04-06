# python

# Create a new mesh container (Mesh_HI)
lx.eval('layer.new')
lx.eval('tool.set prim.cube on 0')
lx.eval('tool.reset prim.cube')
lx.eval('tool.apply')
lx.eval('tool.set prim.cube off 0')
lx.eval('item.name Mesh_HI')
MESH_HI = lx.eval("query sceneservice selection ? locator")

# Create a new mesh container (Mesh_LO)
lx.eval('layer.new')
lx.eval('tool.set prim.cube on 0')
lx.eval('tool.reset prim.cube')
lx.eval('tool.apply')
lx.eval('tool.set prim.cube off 0')
lx.eval('item.name Mesh_LO')
MESH_LO = lx.eval("query sceneservice selection ? locator")
lx.eval('select.drop item')

# Create a new mesh container (Mesh_Decals)
lx.eval('layer.new')
lx.eval('tool.set prim.cube on 0')
lx.eval('tool.reset prim.cube')
lx.eval('tool.apply')
lx.eval('tool.set prim.cube off 0')
lx.eval('item.name Mesh_Decals')
MESH_Decals = lx.eval("query sceneservice selection ? locator")
lx.eval('select.drop item')

### Create RoundEdge material and assign to MESH_HI
lx.eval('select.drop item')
lx.eval('select.subItem ' + MESH_HI + '')
lx.eval('poly.setMaterial RoundEdge {0.8 0.8 0.8} 1.0 0.04 true false')
lx.eval('select.subItem ' + MESH_HI + ' remove')
MAT_RoundEdge = lx.eval1("query sceneservice selection ? all")
# Define RoundEdge material properties
lx.eval('item.channel advancedMaterial$smAngle 25.0')
lx.eval('item.channel advancedMaterial$rndAngle 25.0')
lx.eval('item.channel advancedMaterial$rndWidth 0.01')
lx.eval('item.channel advancedMaterial$rndSame true')
lx.eval('select.subItem ' + MAT_RoundEdge + ' remove')
MASK_MAT_RoundEdge = lx.eval1("query sceneservice selection ? all")

### Cleaning up the default scene ###

# Delete default mesh
lx.eval('select.drop item')
lx.eval('select.subItem mesh002')
lx.eval('delete')
lx.eval('select.drop item')

# Delete default Final Color Output
lx.eval('select.subItem renderOutput020')
lx.eval('delete')

# Delete default Alpha Output
lx.eval('select.subItem renderOutput021')
lx.eval('delete')

### Creating Render Outputs ###

# Create the Alpha Render Output
lx.eval('shader.create renderOutput')
lx.eval('shader.setEffect shade.alpha')
RO_Alpha = lx.eval("query sceneservice selection ? all")

# Create the Diffuse Color Render Output
lx.eval('shader.create renderOutput')
lx.eval('shader.setEffect mat.diffCol')
RO_Diffuse = lx.eval("query sceneservice selection ? all")

# Create the Shading Normal Render Output
lx.eval('shader.create renderOutput')
lx.eval('shader.setEffect shade.normal')
lx.eval('item.channel renderOutput$remap true')
RO_ShadingNormal = lx.eval("query sceneservice selection ? all")

# Create the Ambient Occlusion Render Output
lx.eval('shader.create renderOutput')
lx.eval('shader.setEffect occl.ambient')
lx.eval('item.channel renderOutput$occlRays 1')
RO_AO = lx.eval("query sceneservice selection ? all")

# Create the Surface ID Render Output
lx.eval('shader.create renderOutput')
lx.eval('shader.setEffect geo.surface')
RO_ID = lx.eval("query sceneservice selection ? all")

### Creating texture layers ###

# Create Texture Layer Occlusion (Curvature) 
lx.eval('shader.create occlusion')
lx.eval('item.name Curvature occlusion')
lx.eval('item.channel occlusion$type curvature')
lx.eval('item.channel occlusion$rays 1')
lx.eval('item.channel occlusion$dist 0.1')
#lx.eval('item.channel occlusion$sameSurf true')
TEX_Curvature = lx.eval("query sceneservice selection ? all")

# Create Texture Layer Wireframe Texture
lx.eval('shader.create val.wireframe')
lx.eval('item.channel val.wireframe$edgeMap Seams')
lx.eval('item.channel val.wireframe$transWidth 1.0')
TEX_Wireframe = lx.eval("query sceneservice selection ? all")

# Create Wireframe Texture instance "Wireframe Bump"
lx.eval('texture.instance')
lx.eval('shader.setEffect bump')
lx.eval('item.channel textureLayer$invert true')

### Making sure that MAT_Decals is at top of render tree

### Create "LO" material and assign to MESH_LO
lx.eval('select.drop item')
lx.eval('select.subItem ' + MESH_LO + '')
lx.eval('poly.setMaterial Mesh {1.0 1.0 1.0} 1.0 0.04 true false false')
lx.eval('select.subItem ' + MESH_LO + ' remove')
MAT_LO = lx.eval1("query sceneservice selection ? all")
# Set smoothing angle to 25 degrees
lx.eval('item.channel advancedMaterial$smAngle 25.0')
lx.eval('select.subItem ' + MAT_LO + ' remove')
MASK_MAT_LO = lx.eval1("query sceneservice selection ? all")

# Create "Decals" material and assign to MESH_Decals
lx.eval('select.drop item')
lx.eval('select.subItem ' + MESH_Decals + '')
lx.eval('poly.setMaterial Decals {0.0 0.0 0.0} 1.0 0.04 true false false')
lx.eval('select.subItem ' + MESH_Decals + ' remove')
MAT_Decals = lx.eval1("query sceneservice selection ? all")

### Creating Bake Items ###

# Create World Space Normals Render Output Bake Item
lx.eval('bakeItem.createOutputBake')
lx.eval('item.name "World Space Normals"bakeItemRO')
lx.eval('bakeItem.renderOutput ' + RO_ShadingNormal + '')
BAKE_RO_ShadingNormal = lx.eval("query sceneservice selection ? all")

# Create Curvature (Diffuse Color) Render Output Bake Item
lx.eval('bakeItem.createOutputBake')
lx.eval('item.name "Curvature"bakeItemRO')
lx.eval('bakeItem.renderOutput ' + RO_Diffuse + '')
BAKE_RO_Curvature = lx.eval("query sceneservice selection ? all")

# Create Alpha Mask Bake Item
lx.eval('bakeItem.createOutputBake')
lx.eval('item.name "Alpha Mask"bakeItemRO')
lx.eval('bakeItem.renderOutput ' + RO_Alpha + '')
BAKE_RO_Alpha = lx.eval("query sceneservice selection ? all")

# Create Ambient Occlusion Bake Item
lx.eval('bakeItem.createOutputBake')
lx.eval('item.name "Ambient Occlusion"bakeItemRO')
lx.eval('bakeItem.renderOutput ' + RO_AO + '')
BAKE_RO_AO = lx.eval("query sceneservice selection ? all")

# Create Surface ID Bake Item
lx.eval('bakeItem.createOutputBake')
lx.eval('item.name "Surface ID"bakeItemRO')
lx.eval('bakeItem.renderOutput ' + RO_ID + '')
BAKE_RO_ID = lx.eval("query sceneservice selection ? all")

# Create Decals ID Bake Item
lx.eval('bakeItem.createOutputBake')
lx.eval('item.name "Decals ID"bakeItemRO')
lx.eval('bakeItem.renderOutput '+ RO_ID +'')
BAKE_RO_Decals = lx.eval("query sceneservice selection ? all")

### Creating Texture Bake Items ###

# Create Tangent Space Normals Texture Bake Item
lx.eval('bakeItem.createTextureBake')
lx.eval('item.name "Tangent Space Normals"bakeItemTexture')
lx.eval('item.channel bakeItemTexture$useNormalPreset true')
BAKE_TEX_Normal = lx.eval("query sceneservice selection ? all") 

# Create Displacement Texture Bake Item
lx.eval('bakeItem.createTextureBake')
lx.eval('item.name "Displacement"bakeItemTexture')
BAKE_TEX_Displacement = lx.eval("query sceneservice selection ? all")

### Configuring common bake settings on Bake Items ###

lx.eval('select.drop item')
lx.eval('select.subItem ' + BAKE_RO_ShadingNormal + '')
lx.eval('select.subItem ' + BAKE_RO_Curvature + '')
lx.eval('select.subItem ' + BAKE_RO_Alpha + '')
lx.eval('select.subItem ' + BAKE_RO_AO + '')
lx.eval('select.subItem ' + BAKE_RO_ID + '')
lx.eval('select.subItem ' + BAKE_RO_Decals + '')
lx.eval('item.channel bakeItemRO$bakeFrom true')
lx.eval('item.channel bakeItemRO$hiddenTarget true')
lx.eval('item.channel bakeItemRO$hiddenSource true')
lx.eval('item.channel bakeItemRO$hiddenOutput true')
lx.eval('item.channel bakeItemRO$saveOutputFile true')
lx.eval('item.channel bakeItemRO$distance 0.005')
lx.eval('item.channel bakeItemRO$width 512')
lx.eval('item.channel bakeItemRO$height 512')
lx.eval('bakeItem.setUV Texture')

lx.eval('select.subItem ' + BAKE_TEX_Normal + '')
lx.eval('select.subItem ' + BAKE_TEX_Displacement + '')
lx.eval('item.channel bakeItemTexture$bakeFrom true')
lx.eval('item.channel bakeItemTexture$hiddenTarget true')
lx.eval('item.channel bakeItemTexture$hiddenSource true')
lx.eval('item.channel bakeItemTexture$hiddenOutput true')
lx.eval('item.channel bakeItemTexture$saveOutputFile true')
lx.eval('item.channel bakeItemTexture$distance 0.005')

# Hide non-essential items
lx.eval('shader.setVisible ' + RO_ID + ' false')
lx.eval('shader.setVisible ' + RO_AO + ' false')
lx.eval('shader.setVisible ' + RO_ShadingNormal + ' false')
lx.eval('shader.setVisible ' + RO_Alpha + ' false')

### Project organization ###

# Get project name from user
lx.eval("user.defNew name:UserValue type:string life:momentary")
lx.eval('user.def UserValue dialogname "Set project name"')
lx.eval("user.def UserValue username {Name}")

try:
    lx.eval("?user.value UserValue")
    userResponse = lx.eval("dialog.result ?")
    
except:
    userResponse = lx.eval("dialog.result ?")
    sys.exit()
    
user_input = lx.eval("user.value UserValue ?")
lx.out('Project name:',user_input)

# Rename Mesh_LO to match project name
lx.eval('select.drop item')
lx.eval('select.subItem '+ MESH_LO +' set')
lx.eval('item.name "' + user_input + '"')
lx.eval('select.drop item')

# Rename MESH_HI to match project name
lx.eval('select.subItem '+ MESH_HI +' set')
lx.eval('item.name "' + user_input + '_HI"')
lx.eval('select.drop item')

# Rename MESH_Decals to match project name
lx.eval('select.subItem '+ MESH_Decals +' set')
lx.eval('item.name "' + user_input + '_Decals"')
lx.eval('select.drop item')

# Rename mesh material to match project name
lx.eval('select.subItem '+ MASK_MAT_LO +' set')
lx.eval("dialog.result ok")
lx.eval('texture.name "' + user_input + '"')

# Rename render output file names with project name + suffix
lx.eval('select.subItem '+ BAKE_RO_ShadingNormal +'')
lx.eval('item.channel bakeItemRO$outPattern "' + user_input +'_World_Space_Normals"')
lx.eval('select.drop item')

lx.eval('select.subItem '+ BAKE_RO_Curvature +'')
lx.eval('item.channel bakeItemRO$outPattern "' + user_input +'_Curvature"')
lx.eval('select.drop item')

lx.eval('select.subItem '+ BAKE_RO_ID +'')
lx.eval('item.channel bakeItemRO$outPattern "' + user_input +'_ID"')
lx.eval('select.drop item')

lx.eval('select.subItem '+ BAKE_RO_Alpha +'')
lx.eval('item.channel bakeItemRO$outPattern "' + user_input +'_Mask"')
lx.eval('select.drop item')

lx.eval('select.subItem '+ BAKE_RO_AO +'')
lx.eval('item.channel bakeItemRO$outPattern "' + user_input +'_Ambient_Occlusion"')
lx.eval('select.drop item')

lx.eval('select.subItem '+ BAKE_RO_Decals +'')
lx.eval('item.channel bakeItemRO$outPattern "' + user_input +'_Decals_ID"')
lx.eval('select.drop item')

# Set render output directory (usually project's 'bake' folder)
lx.eval('dialog.setup dir')
lx.eval('dialog.title "Set project bake directory"')
lx.eval('dialog.result "D:\Dropbox"')
lx.eval('dialog.open')
output_dir = lx.eval('dialog.result ?')

# Set output directory on Render Output Bake Items
lx.eval('select.drop item')
lx.eval('select.subItem '+ BAKE_RO_AO +' set')
lx.eval('select.subItem '+ BAKE_RO_Alpha +' set')
lx.eval('select.subItem '+ BAKE_RO_Curvature +' set')
lx.eval('select.subItem '+ BAKE_RO_ID +' set')
lx.eval('select.subItem '+ BAKE_RO_ShadingNormal +' set')
lx.eval('select.subItem '+ BAKE_RO_Decals +' set')
lx.eval('item.channel outLocation "' + output_dir + '"')
lx.eval('select.drop item')

# Make a normal map image and parent it in the MESH_LO material
lx.eval('clip.newStill "' + output_dir + '\\' + user_input + '_Normal_Base.png" x2048 RGB false false {0.0 0.0 0.0} PNG (none)')
lx.eval('select.subItem {' + user_input + '_Normal_Base:videoStill001} set mediaClip')
lx.eval('texture.new clip:{' + user_input +'_Normal_Base:videoStill001}')
lx.eval('select.subItem '+ MASK_MAT_LO +' set')
lx.eval('texture.parent '+ MASK_MAT_LO +'')
lx.eval('select.subItem '+ MASK_MAT_LO +' remove')
lx.eval('item.channel textureLayer(txtrLocator)$projType uv')
lx.eval('texture.setUV Texture')
lx.eval('shader.setEffect normal')
IMG_Normal = lx.evalN("query sceneservice selection ? all")
IMG_Normal = IMG_Normal[2]

# While texture layer is selected, assign normal texture output to TS normal bake item
lx.eval('select.subItem '+ BAKE_TEX_Normal +' set')
lx.eval('bakeItem.texture {}')
lx.eval('bakeItem.setAsTextureOutput 0')
lx.eval('select.drop item')

# Make a Displacement map image and parent it in the MESH_LO material
lx.eval('clip.newStill "' + output_dir + '\\' + user_input + '_Displacement.png" x2048 Grey false false {0.0 0.0 0.0} PNG16 (none)')
lx.eval('select.subItem {' + user_input + '_Displacement:videoStill001} set mediaClip')
lx.eval('texture.new clip:{' + user_input +'_Displacement:videoStill001}')
lx.eval('select.subItem '+ MASK_MAT_LO +' set')
lx.eval('texture.parent '+ MASK_MAT_LO +'')
lx.eval('select.subItem '+ MASK_MAT_LO +' remove')
lx.eval('item.channel textureLayer(txtrLocator)$projType uv')
lx.eval('texture.setUV Texture')
lx.eval('shader.setEffect displace')
IMG_Displacement = lx.evalN("query sceneservice selection ? all")
IMG_Displacement = IMG_Displacement[2]

# Assign Displacement texture output to Displacement bake item
lx.eval('select.subItem '+ BAKE_TEX_Displacement +' set')
lx.eval('bakeItem.texture {}')
lx.eval('bakeItem.setAsTextureOutput 0')
lx.eval('select.drop item')

# Set Displacement/Normal texture layers non-visible
lx.eval('shader.setVisible '+ IMG_Normal +' false')
lx.eval('shader.setVisible '+ IMG_Displacement +' false')

# Delete MESH_HI and MESH_Decals UV maps
lx.eval('select.subItem '+ MESH_HI +'')
lx.eval('select.subItem '+ MESH_Decals +'')
lx.eval('dialog.result ok')
lx.eval('vertMap.delete txuv')
lx.eval('select.drop item')

# Set render frame to 1:1 ratio
lx.eval('render.res 0 1024')
lx.eval('render.res 1 1024')

# Lock the mesh containers
lx.eval('select.subItem '+ MESH_HI +'')
lx.eval('select.subItem '+ MESH_Decals +'')
lx.eval('select.subItem '+MESH_LO+'')
lx.eval('item.channel locator$lock on')

# Print debug text (for use in definitions.py)
lx.out('Mesh_LO:',MESH_LO)
lx.out('Mesh_HI:',MESH_HI)
lx.out('Mesh_Decals:',MESH_Decals)
lx.out('Alpha Output:',RO_Alpha)
lx.out('Diffuse Color Output:',RO_Diffuse)
lx.out('Shading Normal Output:',RO_ShadingNormal)
lx.out('Ambient Occlusion Output:',RO_AO)
lx.out('Surface ID Output:',RO_ID)
lx.out('Curvature Texture Layer:',TEX_Curvature)
lx.out('Wireframe Texture Layer:',TEX_Wireframe)
lx.out('World Space Normals Bake Item:',BAKE_RO_ShadingNormal)
lx.out('Curvature Bake Item:',BAKE_RO_Curvature)
lx.out('Alpha Mask Bake Item:',BAKE_RO_Alpha)
lx.out('Ambient Occlusion Bake Item:',BAKE_RO_AO)
lx.out('Surface ID Bake Item:',BAKE_RO_ID)
lx.out('Decals ID Bake Item:',BAKE_RO_Decals)
lx.out('TS Normals Texture Bake Item:',BAKE_TEX_Normal)
lx.out('Displacement Texture Bake Item:',BAKE_TEX_Displacement)
lx.out('RoundEdge Material:',MAT_RoundEdge)
lx.out('RoundEdge Material Mask:',MASK_MAT_RoundEdge)
lx.out('Mesh_LO Material:',MAT_LO)
lx.out('Mesh_LO Material Mask:',MASK_MAT_LO)
lx.out('Mesh_Decals Material:',MAT_Decals)
lx.out('Displacement Image:',IMG_Displacement)
lx.out('TS Normals Image:',IMG_Normal)

# Make MESH_HI the only item visible in the scene
lx.eval('@show_HI.py')

# Assign bake item sources/targets
lx.eval('@set_sources_targets.py')