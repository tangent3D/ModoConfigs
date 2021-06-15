# python

from definitions import *

getMAT_LO().select(replace=True)
lx.eval('material.smoothCrease false')
lx.eval('material.smoothCrease hardedges:true')

# Set area weighting
lx.eval('material.smoothWeight area true')

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

# # Set the Vertex Normals
# getMESH_LO().select(replace=True)
# lx.eval('select.itemHierarchy')
# lx.eval('vertMap.normals "Vertex Normal" true 1.0 Texture false')

lx.eval('select.drop item')