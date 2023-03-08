# python

from definitions import *

# Set the Vertex Normals. Normalize tangents.
getMESH_LO().select(replace=True)
lx.eval('select.itemHierarchy')
lx.eval('vertMap.normals "Vertex Normal" true 1.0 {} true')

lx.eval('select.drop item')