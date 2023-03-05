# python

from definitions import *

# Set the Vertex Normals. Normalize tangents.
getMESH_LO().select(replace=True)
lx.eval('select.itemHierarchy')
lx.eval('vertMap.normals "Vertex Normal" true 1.0 {} true')

# # Disabled the following because it causes problems with xNormal os2ts?
# # Create Mikk Tangent Basis. Note: Tangent Bases must be added before baking!
# lx.eval('select.vertexMap Texture txuv add')
# lx.eval('mesh.mikktspacegen')

lx.eval('select.drop item')