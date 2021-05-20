# python

from definitions import *

# Set bake sources and targets and corresponding materials 
lx.eval('@set_sources_targets.py')

# Explode to frame 1
lx.eval('@setframe1.lxm')

lx.eval('shader.setVisible '+getTEX_Curvature().id+' false')

lx.eval('select.drop item')

lx.eval('select.subItem '+getBAKE_RO_Alpha().id+' set')

# Don't apply edge bleed to baked texture
lx.eval('pref.value render.bakeBorder 0')

lx.eval('bakeItem.bake true')

# Restore edge bleed
lx.eval('pref.value render.bakeBorder 16')

# Restore Curvature visibility
lx.eval('shader.setVisible '+getTEX_Curvature().id+' true')

# Un-explode to frame 0
lx.eval('@setframe0.lxm')

lx.eval('select.drop item')