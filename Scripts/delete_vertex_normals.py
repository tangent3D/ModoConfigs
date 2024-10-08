#python

from definitions import *

# Clears a Vertex Normal map if it exists.
getMESH_LO().select(replace=True)
lx.eval('select.itemHierarchy')
# Fix to try to select base meshes
lx.eval('@select_base_mesh.py')
modo.Scene().select('locator.LO', False)

try:
	lx.eval('select.vertexMap "Vertex Normal" norm replace')
	lx.eval('vertMap.delete norm')
except:
	pass

try:
	lx.eval('select.vertexMap "Texture" tbas replace')
	lx.eval('vertMap.delete tbas')
except:
	pass

lx.eval('select.drop item')