# python

from definitions import *

TEX_Curvature = getTEX_Curvature() 
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