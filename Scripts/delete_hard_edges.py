# python

from definitions import *

# Clears a Hard Edge map if it exists.
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

lx.eval('select.drop item')