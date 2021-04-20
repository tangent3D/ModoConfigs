# python

from definitions import *

lx.eval('unhide')
getMESH_HI().select(replace=True)
getMESH_LO().select()
lx.eval('select.itemHierarchy')
lx.eval('hide.unsel')
getMESH_LO().select(replace=True)