# python

from definitions import *

getMESH_HI().select(replace=True)
getMESH_Decals().select()
lx.eval('select.itemHierarchy')
lx.eval('unhide')

getMESH_Decals().select(replace=True)
lx.eval('select.itemHierarchy')
lx.eval('hide.sel')

getMESH_LO().select(replace=True)
lx.eval('select.itemHierarchy')
lx.eval('unhide')