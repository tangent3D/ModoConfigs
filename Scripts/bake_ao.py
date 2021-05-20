# python

from definitions import *

# Set bake sources and targets and corresponding materials 
lx.eval('@set_sources_targets.py')

# Do not explode!
lx.eval('@setframe0.lxm')

# Hide curvature layer
lx.eval('shader.setVisible '+getTEX_Curvature().id+' false')

# Define baked occlusion rays
getRO_AO().select(replace=True)
lx.eval('item.channel renderOutput$occlRays 128')

# Set RoundEdge material to double sided
getMAT_RoundEdge().select(replace=True)
lx.eval('item.channel advancedMaterial$dblSided true')

# Bake the Ambient Occlusion Render Output
getBAKE_RO_AO().select(replace=True)
lx.eval('bakeItem.bake true')

# Restore RoundEdge material to one sided
getMAT_RoundEdge().select(replace=True)
lx.eval('item.channel advancedMaterial$dblSided false')

# Restore curvature layer visibility
lx.eval('shader.setVisible '+getTEX_Curvature().id+' true')

lx.eval('select.drop item')