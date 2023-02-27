# python

from definitions import *

# Don't display deformers
lx.eval('view3d.enableDeformers false')

lx.eval('select.type item')
lx.eval('unhide')
getMESH_LO().select(replace=True)
lx.eval('select.itemHierarchy')
lx.eval('hide.unsel')
lx.eval('select.vertexMap Texture txuv add')