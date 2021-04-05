# python

from definitions import *

# Set sources
# Assign RoundEdge material to HP mesh and all children
lx.eval('select.drop item')
lx.eval('select.subItem '+Mesh_HI+'')
lx.eval('select.itemHierarchy')
lx.eval('poly.setMaterial RoundEdge {0.8 0.8 0.8} 1.0 0.04 true false false')

lx.eval('select.subitem ' + BAKE_TEX_Normal + ' remove')
lx.eval('select.subitem ' + BAKE_TEX_Displacement + ' remove')

lx.eval('select.subItem ' + BAKE_RO_ShadingNormal + ' set')
lx.eval('select.subItem ' + BAKE_RO_Curvature + ' set')
lx.eval('select.subItem ' + BAKE_RO_Alpha + ' set')
lx.eval('select.subItem ' + BAKE_RO_AO + ' set')
lx.eval('select.subItem ' + BAKE_RO_ID + ' set')

lx.eval('bakeItem.source {} type:1')
lx.eval('bakeItem.setAsSource 0 1 0')
lx.eval('bakeItem.setUV Texture')

lx.eval('select.subItem ' + BAKE_RO_ShadingNormal + ' remove')
lx.eval('select.subItem ' + BAKE_RO_Curvature + ' remove')
lx.eval('select.subItem ' + BAKE_RO_Alpha + ' remove')
lx.eval('select.subItem ' + BAKE_RO_AO + ' remove')
lx.eval('select.subItem ' + BAKE_RO_ID + ' remove')

lx.eval('select.subitem ' + BAKE_TEX_Normal + ' set')
lx.eval('select.subitem ' + BAKE_TEX_Displacement + ' set')

lx.eval('bakeItem.source {} type:0')
lx.eval('bakeItem.setAsSource 0 0 0')

lx.eval('select.drop item')

# Set targets
# Assign LP material to LP mesh and all children
lx.eval('select.subItem '+MESH_LO+'')
name = lx.eval('item.name ?')
lx.eval('select.itemHierarchy')
lx.eval('poly.setMaterial '+name+' {1.0 1.0 1.0} 1.0 0.04 true false')

lx.eval('select.subitem ' + BAKE_TEX_Normal + ' remove')
lx.eval('select.subitem ' + BAKE_TEX_Displacement + ' remove')

lx.eval('select.subItem ' + BAKE_RO_ShadingNormal + ' set')
lx.eval('select.subItem ' + BAKE_RO_Curvature + ' set')
lx.eval('select.subItem ' + BAKE_RO_Alpha + ' set')
lx.eval('select.subItem ' + BAKE_RO_AO + ' set')
lx.eval('select.subItem ' + BAKE_RO_ID + ' set')
lx.eval('select.subItem ' + BAKE_RO_Decals + ' set')

lx.eval('bakeItem.target {} type:1')
lx.eval('bakeItem.setAsTarget 0 1 0')
lx.eval('bakeItem.setUV Texture')

lx.eval('select.subItem ' + BAKE_RO_ShadingNormal + ' remove')
lx.eval('select.subItem ' + BAKE_RO_Curvature + ' remove')
lx.eval('select.subItem ' + BAKE_RO_Alpha + ' remove')
lx.eval('select.subItem ' + BAKE_RO_AO + ' remove')
lx.eval('select.subItem ' + BAKE_RO_ID + ' remove')

lx.eval('select.subitem ' + BAKE_TEX_Normal + ' set')
lx.eval('select.subitem ' + BAKE_TEX_Displacement + ' set')

lx.eval('bakeItem.target {} type:0')
lx.eval('bakeItem.setAsTarget 0 0 0')

lx.eval('select.drop item')

# Set decals sources and materials
lx.eval('select.subItem '+ MESH_Decals +'')
lx.eval('select.itemHierarchy')
lx.eval('poly.setMaterial Decals {0.0 0.0 0.0} 1.0 0.04 true false false')
lx.eval('select.subItem ' + BAKE_RO_Decals + ' set')

lx.eval('bakeItem.source {} type:1')
lx.eval('bakeItem.setAsSource 0 1 0')
lx.eval('bakeItem.setUV Texture')

lx.eval('select.drop item')