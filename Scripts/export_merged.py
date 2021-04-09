# python

from definitions import *

projectName = getProjectName()
MESH_LO = getMESH_LO()
MESH_HI = getMESH_HI()
MESH_Decals = getMESH_Decals()
MASK_MAT_LO = getMASK_MAT_LO()
MAT_LO = getMAT_LO()
MASK_MAT_RoundEdge = getMASK_MAT_RoundEdge()
MAT_RoundEdge = getMAT_RoundEdge()
RO_Alpha = getRO_Alpha()
RO_Diffuse = getRO_Diffuse()
RO_ShadingNormal = getRO_ShadingNormal()
RO_ID = getRO_ID()
TEX_Curvature = getTEX_Curvature() 
TEX_Wireframe = getTEX_Wireframe()
BAKE_RO_ShadingNormal = getBAKE_RO_ShadingNormal()
BAKE_RO_Curvature = getBAKE_RO_Curvature()
BAKE_RO_Alpha = getBAKE_RO_Alpha()
BAKE_RO_ID = getBAKE_RO_ID()
BAKE_RO_Decals = getBAKE_RO_Decals()
BAKE_TEX_Normal = getBAKE_TEX_Normal()
IMG_Normal = getIMG_Normal()

scene = modo.Scene()

MESH_LO.select(replace=True)
lx.eval('select.itemHierarchy')
# Deselect the locator so it's not merged
modo.item.Item('locator.LO').deselect()
lx.eval('vertMap.normals "Vertex Normal" true 1.0 {} false')
lx.eval('item.duplicate false locator false true')
lx.eval('layer.mergeMeshes true')
mergedMesh = modo.item.Item(item=None)
lx.eval('export.selected 15 false false false')
# Select original scene
modo.scene.Scene(scene=scene.scene)
mergedMesh.select(replace=True)
lx.eval('item.channel locator$lock off')
lx.eval('delete')