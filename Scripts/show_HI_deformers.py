# python

from definitions import *

# Show deformers
lx.eval('view3d.enableDeformers true')

lx.eval('select.type item')
lx.eval('unhide')
getMESH_HI().select(replace=True)
lx.eval('select.itemHierarchy')
lx.eval('hide.unsel')