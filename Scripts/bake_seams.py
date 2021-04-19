# python

from definitions import *

# Set bake sources and targets and corresponding materials 
lx.eval('@set_sources_targets.py')

# Set bake settings final
lx.eval('@bake_settings_final.py')

# Explode to frame 1
lx.eval('select.time 0.041667 0 0')

lx.eval('shader.setVisible '+getTEX_Curvature().id+' false')

# Invert the wireframe texture layer so it'll bake out as a mask
getTEX_Wireframe().select(replace=True)
lx.eval('item.channel textureLayer$invert true')

lx.eval('select.drop item')
lx.eval('select.subItem '+getBAKE_RO_Seams().id+' set')
lx.eval('bakeItem.bake true')

# Un-invert the wireframe texture layer
getTEX_Wireframe().select(replace=True)
lx.eval('item.channel textureLayer$invert false')

lx.eval('shader.setVisible '+getTEX_Curvature().id+' true')

# Un-explode to frame 0
lx.eval('select.time 0 0 0')

lx.eval('select.drop item')