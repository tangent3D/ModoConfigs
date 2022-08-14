# python

from definitions import *

# Don't display deformers
lx.eval('view3d.enableDeformers false')

lx.eval('unhide')
getMESH_HI().select(replace=True)
getMESH_Decals().select()
getMESH_LO().select()
lx.eval('select.itemHierarchy')
lx.eval('deformer.selectBaseMesh')
lx.eval('hide.unsel')