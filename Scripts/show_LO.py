# python

from definitions import *

lx.eval('unhide')
getMESH_LO().select(replace=True)
lx.eval('select.itemHierarchy')
lx.eval('hide.unsel')
lx.eval('select.vertexMap Texture txuv add')