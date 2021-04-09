# python

from definitions import *

MESH_Decals = getMESH_Decals()
MESH_HI = getMESH_HI()
MESH_LO = getMESH_LO()
BAKE_RO_ShadingNormal = getBAKE_RO_ShadingNormal()
BAKE_RO_Curvature = getBAKE_RO_Curvature()
BAKE_RO_Alpha = getBAKE_RO_Alpha()
BAKE_RO_ID = getBAKE_RO_ID()
BAKE_RO_Decals = getBAKE_RO_Decals()
BAKE_TEX_Normal = getBAKE_TEX_Normal()

# Set sources
# Assign RoundEdge material to HP mesh and all children
MESH_HI.select(replace=True)
lx.eval('select.itemHierarchy')
lx.eval('poly.setMaterial RoundEdge {0.8 0.8 0.8} 1.0 0.04 true false false')

BAKE_RO_ShadingNormal.select()
BAKE_RO_Curvature.select()
BAKE_RO_Alpha.select()
BAKE_RO_ID.select()

lx.eval('bakeItem.source {} type:1')
lx.eval('bakeItem.setAsSource 0 1 0')
lx.eval('bakeItem.setUV Texture')

MESH_HI.select(replace=True)
lx.eval('select.itemHierarchy')
BAKE_TEX_Normal.select()

lx.eval('bakeItem.source {} type:0')
lx.eval('bakeItem.setAsSource 0 0 0')

# Set targets

# Assign LP material to LP mesh and all children
MESH_LO.select(replace=True)
name = lx.eval('item.name ?')
lx.eval('select.itemHierarchy')
lx.eval('poly.setMaterial '+name+' {1.0 1.0 1.0} 1.0 0.04 true false')

BAKE_RO_ShadingNormal.select()
BAKE_RO_Curvature.select()
BAKE_RO_Alpha.select()
BAKE_RO_ID.select()
BAKE_RO_Decals.select()

lx.eval('bakeItem.target {} type:1')
lx.eval('bakeItem.setAsTarget 0 1 0')
lx.eval('bakeItem.setUV Texture')

# Set Tangent Space Normals stuff
MESH_LO.select(replace=True)
lx.eval('select.itemHierarchy')
BAKE_TEX_Normal.select()
lx.eval('bakeItem.target {} type:0')
lx.eval('bakeItem.setAsTarget 0 0 0')

# Set decals sources and materials
MESH_Decals.select(replace=True)
lx.eval('select.itemHierarchy')
lx.eval('poly.setMaterial Decals {0.0 0.0 0.0} 1.0 0.04 true false false')

BAKE_RO_Decals.select()
lx.eval('bakeItem.source {} type:1')
lx.eval('bakeItem.setAsSource 0 1 0')
lx.eval('bakeItem.setUV Texture')

lx.eval('select.drop item')