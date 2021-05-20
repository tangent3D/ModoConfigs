# python

from definitions import *

# Set bake sources and targets and corresponding materials 
lx.eval('@set_sources_targets.py')

# Explode to frame 1
lx.eval('@setframe1.lxm')

# Define baked Curvature occlusion rays
getTEX_Curvature().select(replace=True)
lx.eval('item.channel occlusion$rays 32')

lx.eval('shader.setVisible '+getTEX_Wireframe().id+' false')

lx.eval('shader.setVisible '+getTEX_Curvature().id+' true')

lx.eval('select.drop item')

lx.eval('select.subItem '+getBAKE_RO_Curvature().id+' set')

lx.eval('bakeItem.bake true')

# Restore Curvature occlusion rays to 1
getTEX_Curvature().select(replace=True)
lx.eval('item.channel occlusion$rays 1')

lx.eval('shader.setVisible '+getTEX_Wireframe().id+' true')

# Un-explode to frame 0
lx.eval('@setframe0.lxm')

lx.eval('select.drop item')