# python

from definitions import *

getMESH_HI().select(replace=True)
getMESH_Decals().select()
getMESH_LO().select()
lx.eval('select.itemHierarchy')
lx.eval('unhide')
lx.eval('select.drop item')