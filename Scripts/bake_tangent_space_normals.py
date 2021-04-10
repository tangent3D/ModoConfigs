# python

from definitions import *

# Set bake sources and targets and corresponding materials 
lx.eval('@set_sources_targets.py')

lx.eval('shader.setVisible '+getTEX_Curvature().id+' false')
getBAKE_TEX_Normal().select(replace=True)
lx.eval('bakeItem.bake true')
lx.eval('shader.setVisible '+getTEX_Curvature().id+' true')
lx.eval('shader.setVisible '+getIMG_Normal().id+' true')

lx.eval('@show_LO.py')