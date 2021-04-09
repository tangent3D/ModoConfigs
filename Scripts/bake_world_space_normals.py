# python

from definitions import *

TEX_Curvature = getTEX_Curvature() 
BAKE_RO_ShadingNormal = getBAKE_RO_ShadingNormal()

# Set bake sources and targets and corresponding materials 
lx.eval('@set_sources_targets.py')

# Set bake settings final
lx.eval('@bake_settings_final.py')

# Explode to frame 1
lx.eval('select.time 0.041667 0 0')

lx.eval('shader.setVisible '+TEX_Curvature.id+' false')

BAKE_RO_ShadingNormal.select(replace=True)

lx.eval('bakeItem.bake true')

lx.eval('shader.setVisible '+TEX_Curvature.id+' true')

# Un-explode to frame 0
lx.eval('select.time 0 0 0')

lx.eval('select.drop item')