# python

from definitions import *

lx.eval('select.drop item')
lx.eval('select.subItem '+MESH_LO+'')
lx.eval('select.itemHierarchy')
lx.eval('unhide')
lx.eval('select.drop item')

lx.eval('select.subItem '+Mesh_HI+'')
lx.eval('select.itemHierarchy')
lx.eval('hide.sel')
lx.eval('select.drop item')

lx.eval('select.subItem '+MESH_LO+'')
lx.eval('select.drop item')