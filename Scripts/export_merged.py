# python

from definitions import *

# Mesh022 (from Mesh_LO initialized by initialize_project.py) must be parent mesh.
# Scene must be Scene 1 (topmost) for script to complete cleanup after export.

lx.eval('select.drop item')
lx.eval('select.subItem ' + MESH_LO + ' add')
lx.eval('select.itemHierarchy')
lx.eval('vertMap.normals "Vertex Normal" true 1.0 {} false')
lx.eval('item.duplicate false locator false true')
lx.eval('layer.mergeMeshes true')
mergedMesh = lx.eval("query sceneservice selection ? locator")
lx.eval('export.selected 15 false false false')
lx.eval('scene.set 1')
lx.eval('select.drop item')
lx.eval('select.subItem '+ mergedMesh +'')
lx.eval('item.channel locator$lock off')
lx.eval('delete')