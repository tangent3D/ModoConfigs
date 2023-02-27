# python

from definitions import *

# Note: Items outside of HI, LO, Decals hierarchies will retain their assigned material.

lx.eval('select.drop item')

# Assign RoundEdge material to HP mesh and all children.
# Assigns materials to MeshOp item base meshes.
getMESH_HI().select(replace=True)
lx.eval('select.itemHierarchy')
for item in modo.Scene().selected:
	lx.eval('select.drop item')
	if item.type == 'mesh':
		lx.eval('select.subItem '+item.id+' set')
		lx.eval('deformer.selectBaseMesh')
		lx.eval('select.deformer '+item.id+' remove')
		# RoundEdge material parameters
		lx.eval('poly.setMaterial RoundEdge {1.0 1.0 1.0} 1.0 0.04 true false false')

# Assign Decals material to Decals mesh and all children
getMESH_Decals().select(replace=True)
lx.eval('select.itemHierarchy')
lx.eval('poly.setMaterial Decals {0.0 0.0 0.0} 1.0 0.04 true false false')
lx.eval('select.drop item')
