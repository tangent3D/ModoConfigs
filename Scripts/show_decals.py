# python

from definitions import *

# Don't display deformers
lx.eval('view3d.enableDeformers false')

lx.eval('select.type item')
lx.eval('unhide')
getMESH_Decals().select(replace=True)
lx.eval('select.itemHierarchy')
lx.eval('hide.unsel')