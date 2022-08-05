# python

from definitions import *

# Note: Items outside of HI, LO, Decals hierarchies will retain their assigned material.

# Assign RoundEdge material to HP mesh and all children
getMESH_HI().select(replace=True)
lx.eval('select.itemHierarchy')
lx.eval('poly.setMaterial RoundEdge {1.0 1.0 1.0} 1.0 0.04 true false false')
lx.eval('select.drop item')

# Assign LO material to LO mesh and all children
getMESH_LO().select(replace=True)
name = lx.eval('item.name ?')
lx.eval('select.itemHierarchy')
lx.eval('poly.setMaterial '+name+' {0.0 0.0 0.0} 1.0 2.0 true false false')
# High contrast material for normal map debugging
getMAT_LO().select(replace=True)
lx.eval('item.channel advancedMaterial$rough 1.0')
lx.eval('select.drop item')

# Assign Decals material to Decals mesh and all children
getMESH_Decals().select(replace=True)
lx.eval('select.itemHierarchy')
lx.eval('poly.setMaterial Decals {0.0 0.0 0.0} 1.0 0.04 true false false')
lx.eval('select.drop item')
