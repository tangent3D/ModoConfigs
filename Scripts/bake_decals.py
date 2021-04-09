# python

from definitions import *

TEX_Curvature = getTEX_Curvature() 
BAKE_RO_Decals = getBAKE_RO_Decals()

# Set bake sources and targets and corresponding materials 
lx.eval('@set_sources_targets.py')

# Explode to frame 1
lx.eval('select.time 0.041667 0 0')

lx.eval('shader.setVisible '+TEX_Curvature.id+' false')

lx.eval('select.drop item')

lx.eval('select.subItem '+BAKE_RO_Decals.id+' set')

# Set bake resolution to 4096x4096px
lx.eval('item.channel bakeItemRO$width 4096')
lx.eval('item.channel bakeItemRO$height 4096')

# Don't apply edge bleed to baked texture
lx.eval('pref.value render.bakeBorder 0')

lx.eval('bakeItem.bake true')

# Restore bake border
lx.eval('pref.value render.bakeBorder 16')

lx.eval('shader.setVisible '+TEX_Curvature.id+' true')

# Un-explode to frame 0
lx.eval('select.time 0 0 0')

lx.eval('select.drop item')