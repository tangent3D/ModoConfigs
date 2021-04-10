# python

from definitions import *

getMESH_Decals().select(replace=True)
lx.eval('select.itemHierarchy')
lx.eval('unhide')
lx.eval('select.drop item')

getMESH_LO().select(replace=True)
getMESH_HI().select()
lx.eval('select.itemHierarchy')
lx.eval('hide.sel')

getMESH_Decals().select(replace=True)
lx.eval('select.itemHierarchy')