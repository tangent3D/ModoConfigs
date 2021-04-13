# python

from definitions import *

getMAT_LO().select(replace=True)
lx.eval('material.smoothCrease false')
lx.eval('material.smoothCrease hardedges:true')

# Set area weighting
lx.eval('material.smoothWeight area true')

getMESH_LO().select(replace=True)
lx.eval('select.itemHierarchy')
lx.eval('select.vertexMap Texture txuv replace')
lx.eval('hardedge.setDefault uvisland')
lx.eval('hardedge.setDefault soft:uvisland')
lx.eval('hardedge.set soft')
lx.eval('hardedge.set hard')

lx.eval('select.drop item')