# python

from definitions import *

getMESH_HI().select(replace=True)
lx.eval('select.itemHierarchy')
lx.eval('unhide')

getMESH_LO().select(replace=True)
getMESH_Decals().select()
lx.eval('select.itemHierarchy')
lx.eval('hide.sel')

getMESH_HI().select(replace=True)
lx.eval('select.itemHierarchy')