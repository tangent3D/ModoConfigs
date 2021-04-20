# python

from definitions import *

lx.eval('unhide')
getMESH_HI().select(replace=True)
getMESH_Decals().select()
lx.eval('select.itemHierarchy')
lx.eval('hide.unsel')
getMESH_Decals().select(replace=True)