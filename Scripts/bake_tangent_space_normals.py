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

# Set bake sources and targets and corresponding materials 
lx.eval('@set_sources_targets.py')

lx.eval('shader.setVisible '+TEX_Curvature.id+' false')
BAKE_TEX_Normal.select(replace=True)
lx.eval('bakeItem.bake true')
lx.eval('shader.setVisible '+TEX_Curvature.id+' true')
lx.eval('shader.setVisible '+IMG_Normal.id+' true')

lx.eval('@show_LO.py')