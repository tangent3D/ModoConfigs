# python

from definitions import *

lx.eval('select.subItem '+ MAT_LO +'')
lx.eval('material.smoothCrease false')
lx.eval('material.smoothCrease hardedges:true')

# Set area weighting
lx.eval('material.smoothWeight area true')

lx.eval('select.subItem '+ MESH_LO +'')
lx.eval('select.vertexMap Texture txuv replace')
lx.eval('hardedge.setDefault uvisland')
lx.eval('hardedge.setDefault soft:uvisland')
lx.eval('hardedge.set soft')
lx.eval('hardedge.set hard')
lx.eval('select.drop item')