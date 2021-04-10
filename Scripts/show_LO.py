# python

from definitions import *

getMESH_LO().select(replace=True)
lx.eval('select.itemHierarchy')
lx.eval('unhide')

getMESH_HI().select(replace=True)
getMESH_Decals().select()
lx.eval('select.itemHierarchy')
lx.eval('hide.sel')

getMESH_LO().select(replace=True)
lx.eval('select.vertexMap Texture txuv replace')
lx.eval('select.itemHierarchy')