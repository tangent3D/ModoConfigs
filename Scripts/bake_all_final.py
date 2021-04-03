# python

from definitions import *

# Set bake sources and targets and corresponding materials 
lx.eval('@set_sources_targets.py')

# Set bake settings final
lx.eval('@bake_settings_final.py')

# Explode to frame 1
lx.eval('select.time 0.041667 0 0')

lx.eval('@bake_curvature.py')

lx.eval('@bake_world_space_normals.py')

lx.eval('@bake_tangent_space_normals.py')

# Restore bake settings to draft quality
lx.eval('@bake_settings_draft.py')

# Un-explode to frame 0
lx.eval('select.time 0 0 0')

lx.eval('select.drop item')