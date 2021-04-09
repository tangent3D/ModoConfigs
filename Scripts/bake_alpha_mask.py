# python

from definitions import *

TEX_Curvature = getTEX_Curvature()
BAKE_RO_Alpha = getBAKE_RO_Alpha()

# Set bake sources and targets and corresponding materials 
lx.eval('@set_sources_targets.py')

# Set bake settings final for 2048*2px
lx.eval('@bake_settings_final.py')

# Explode to frame 1
lx.eval('select.time 0.041667 0 0')

lx.eval('shader.setVisible '+TEX_Curvature.id+' false')

lx.eval('select.drop item')

lx.eval('select.subItem '+BAKE_RO_Alpha.id+' set')

# Don't apply edge bleed to baked texture
lx.eval('pref.value render.bakeBorder 0')

lx.eval('bakeItem.bake true')

lx.eval('pref.value render.bakeBorder 16')

# Restore bake settings to draft
lx.eval('@bake_settings_draft.py')

lx.eval('shader.setVisible '+TEX_Curvature.id+' true')

# Un-explode to frame 0
lx.eval('select.time 0 0 0')

lx.eval('select.drop item')