# python

from definitions import *

MESH_LO = getMESH_LO()
MESH_HI = getMESH_HI()
MESH_Decals = getMESH_Decals()

MESH_Decals.select(replace=True)
lx.eval('select.itemHierarchy')
lx.eval('unhide')
lx.eval('select.drop item')

MESH_LO.select(replace=True)
MESH_HI.select()
lx.eval('select.itemHierarchy')
lx.eval('hide.sel')

MESH_Decals.select(replace=True)