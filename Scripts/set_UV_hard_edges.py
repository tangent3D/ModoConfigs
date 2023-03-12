# python

from definitions import *

# Before we set the hard edges, let's make sure to remove any existing Normal or Hard Edge vertex maps
getMESH_LO().select(replace=True)
lx.eval('select.itemHierarchy')

try:
	lx.eval('select.vertexMap "Hard Edge" hard replace')
	lx.eval('vertMap.delete hard')
except:
	pass

try:
	lx.eval('select.vertexMap "Vertex Normal" norm replace')
	lx.eval('vertMap.delete norm')
except:
	pass

# Define the new hard edges
getMESH_LO().select(replace=True)
lx.eval('select.itemHierarchy')
lx.eval('select.vertexMap Texture txuv replace')
lx.eval('hardedge.setDefault uvisland')
lx.eval('hardedge.setDefault soft:uvisland')
lx.eval('hardedge.set soft')
lx.eval('hardedge.set hard')

lx.eval('select.drop item')