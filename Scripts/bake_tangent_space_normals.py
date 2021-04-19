# python

from definitions import *

# Set bake sources and targets and corresponding materials 
lx.eval('@set_sources_targets.py')

# Explode to frame 1
lx.eval('select.time 0.041667 0 0')

lx.eval('shader.setVisible '+getTEX_Curvature().id+' false')
getBAKE_TEX_Normal().select(replace=True)
lx.eval('bakeItem.bake true')
lx.eval('shader.setVisible '+getTEX_Curvature().id+' true')
lx.eval('shader.setVisible '+getIMG_Normal().id+' true')

# Un-explode to frame 0
lx.eval('select.time 0 0 0')

lx.eval('@show_LO.py')