# python

from definitions import *

scene = modo.Scene()

getMESH_LO().select(replace=True)
lx.eval('select.itemHierarchy')
# Deselect the locator so it's not merged
modo.item.Item('locator.LO').deselect()
lx.eval('vertMap.normals "Vertex Normal" true 1.0 {} false')
lx.eval('item.duplicate false locator false true')
lx.eval('layer.mergeMeshes true')
mergedMesh = modo.item.Item(item=None)
try:
	lx.eval('export.selected 15 false false false')
except:
	pass
# Select original scene
modo.scene.Scene(scene=scene.scene)
mergedMesh.select(replace=True)
lx.eval('delete')