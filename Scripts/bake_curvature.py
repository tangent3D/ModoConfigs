# python

from definitions import *

# Set bake sources and targets and corresponding materials 
lx.eval('@set_sources_targets.py')

# Set bake settings final
lx.eval('@bake_settings_final.py')

# Explode to frame 1
lx.eval('select.time 0.041667 0 0')

lx.eval('shader.setVisible '+ TEX_Curvature +' true')

lx.eval('select.drop item')

lx.eval('select.subItem '+ BAKE_RO_Curvature +' set')

lx.eval('bakeItem.bake true')

# Un-explode to frame 0
lx.eval('select.time 0 0 0')

lx.eval('select.drop item')