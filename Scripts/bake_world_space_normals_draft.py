# python

from definitions import *

# Set bake sources and targets and corresponding materials 
lx.eval('@set_sources_targets.py')

# Set bake settings draft
lx.eval('@bake_settings_draft.py')

# Explode to frame 1
lx.eval('select.time 0.041667 0 0')

lx.eval('shader.setVisible '+getTEX_Curvature().id+' false')

getBAKE_RO_ShadingNormal().select(replace=True)

lx.eval('bakeItem.bake true')

lx.eval('shader.setVisible '+getTEX_Curvature().id+' true')

# Un-explode to frame 0
lx.eval('select.time 0 0 0')

lx.eval('select.drop item')