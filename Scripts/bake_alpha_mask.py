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

# Set bake settings final for 2048*2px
lx.eval('@bake_settings_final.py')

# Explode to frame 1
lx.eval('select.time 0.041667 0 0')

lx.eval('shader.setVisible '+TEX_Curvature.id+' false')

lx.eval('select.drop item')

lx.eval('select.subItem '+BAKE_RO_Alpha.id+' set')

# Don't apply edge bleed to baked texture
lx.eval('pref.value render.bakeBorder 0')

lx.eval('bakeItem.bake true')

lx.eval('pref.value render.bakeBorder 16')

# Restore bake settings to draft
lx.eval('@bake_settings_draft.py')

lx.eval('shader.setVisible '+TEX_Curvature.id+' true')

# Un-explode to frame 0
lx.eval('select.time 0 0 0')

lx.eval('select.drop item')