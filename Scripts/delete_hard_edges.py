#python

from definitions import *

# Clears a Hard Edges map if it exists.
getMESH_LO().select(replace=True)
lx.eval('select.itemHierarchy')
lx.eval('select.vertexMap "Hard Edge" hard replace')
lx.eval('vertMap.delete hard')
lx.eval('select.drop item')