# python

from definitions import *

lx.eval('select.drop item')

# Remove UV map 'Texture' from all HI and Decal meshes
getMESH_HI().select(replace=True)
getMESH_Decals().select()
lx.eval('select.itemHierarchy')

try:
	lx.eval('select.vertexMap Texture txuv add')
	lx.eval('vertMap.delete txuv')
except:
	pass

lx.eval('select.drop item')