# python

from definitions import *

MESH_LO = getMESH_LO()
MESH_HI = getMESH_HI()
MESH_Decals = getMESH_Decals()

MESH_HI.select(replace=True)
lx.eval('select.itemHierarchy')
lx.eval('unhide')

MESH_LO.select(replace=True)
MESH_Decals.select()
lx.eval('select.itemHierarchy')
lx.eval('hide.sel')

MESH_HI.select(replace=True)