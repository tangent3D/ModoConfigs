# python

from definitions import *

projectName = getProjectName()
MESH_LO = getMESH_LO()
MESH_HI = getMESH_HI()
MESH_Decals = getMESH_Decals()
MASK_MAT_LO = getMASK_MAT_LO()
MAT_LO = getMAT_LO()
MASK_MAT_RoundEdge = getMASK_MAT_RoundEdge()
MAT_RoundEdge = getMAT_RoundEdge()
RO_Alpha = getRO_Alpha()
RO_Diffuse = getRO_Diffuse()
RO_ShadingNormal = getRO_ShadingNormal()
RO_ID = getRO_ID()
TEX_Curvature = getTEX_Curvature() 
TEX_Wireframe = getTEX_Wireframe()
BAKE_RO_ShadingNormal = getBAKE_RO_ShadingNormal()
BAKE_RO_Curvature = getBAKE_RO_Curvature()
BAKE_RO_Alpha = getBAKE_RO_Alpha()
BAKE_RO_ID = getBAKE_RO_ID()
BAKE_RO_Decals = getBAKE_RO_Decals()
BAKE_TEX_Normal = getBAKE_TEX_Normal()
IMG_Normal = getIMG_Normal()

# Get desired round edge width from user
lx.eval("user.defNew name:UserValue type:string life:momentary")
lx.eval('user.def UserValue dialogname "Set round edge width"')
lx.eval("user.def UserValue username {Round edge width (meters)}")

try:
    lx.eval("?user.value UserValue")
    userResponse = lx.eval("dialog.result ?")
    
except:
    userResponse = lx.eval("dialog.result ?")
    sys.exit()
    
user_input = lx.eval("user.value UserValue ?")
lx.out('Round edge width:',user_input)

# Set RoundEdge material width
MAT_RoundEdge.select(replace=True)
lx.eval('item.channel advancedMaterial$rndWidth '+ user_input +'')

# Set Curvature Occlusion Distance to RE width * 10
occlusionDistance = float(user_input)
occlusionDistance = (occlusionDistance * 10)
occlusionDistance = str(occlusionDistance)
TEX_Curvature.select(replace=True)
lx.eval('item.channel occlusion$dist ' + occlusionDistance + '')

# Set Wireframe Texture line width to RE width / 2
lineWidth = float(user_input)
lineWidth = (lineWidth / 2)
lineWidth = str(lineWidth)
TEX_Wireframe.select(replace=True)
lx.eval('item.channel val.wireframe$width '+ lineWidth +'')

lx.eval('select.drop item')