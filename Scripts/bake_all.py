# python

from definitions import *

# Automate baking of all textures as required

# Set bake sources and targets and corresponding materials 
lx.eval('@set_sources_targets.py')

lx.eval('@bake_world_space_normals.py')

lx.eval('@bake_tangent_space_normals.py')

lx.eval('@bake_curvature.py')

lx.eval('@bake_seams.py')

lx.eval('@bake_ID.py')

lx.eval('@bake_ao.py')

lx.eval('@bake_decals.py')

lx.eval('select.drop item')