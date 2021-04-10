# python

from definitions import *

# Set sources
# Assign RoundEdge material to HP mesh and all children
getMESH_HI().select(replace=True)
lx.eval('select.itemHierarchy')
lx.eval('poly.setMaterial RoundEdge {0.8 0.8 0.8} 1.0 0.04 true false false')

getBAKE_RO_ShadingNormal().select()
getBAKE_RO_Curvature().select()
getBAKE_RO_Alpha().select()
getBAKE_RO_ID().select()

lx.eval('bakeItem.source {} type:1')
lx.eval('bakeItem.setAsSource 0 1 0')
lx.eval('bakeItem.setUV Texture')

getMESH_HI().select(replace=True)
lx.eval('select.itemHierarchy')
getBAKE_TEX_Normal().select()

lx.eval('bakeItem.source {} type:0')
lx.eval('bakeItem.setAsSource 0 0 0')

# Set targets

# Assign LP material to LP mesh and all children
getMESH_LO().select(replace=True)
name = lx.eval('item.name ?')
lx.eval('select.itemHierarchy')
lx.eval('poly.setMaterial '+name+' {1.0 1.0 1.0} 1.0 0.04 true false')

getBAKE_RO_ShadingNormal().select()
getBAKE_RO_Curvature().select()
getBAKE_RO_Alpha().select()
getBAKE_RO_ID().select()
getBAKE_RO_Decals().select()

lx.eval('bakeItem.target {} type:1')
lx.eval('bakeItem.setAsTarget 0 1 0')
lx.eval('bakeItem.setUV Texture')

# Set Tangent Space Normals stuff
getMESH_LO().select(replace=True)
lx.eval('select.itemHierarchy')
getBAKE_TEX_Normal().select()
lx.eval('bakeItem.target {} type:0')
lx.eval('bakeItem.setAsTarget 0 0 0')

getBAKE_TEX_Normal().select(replace=True)
lx.eval('bakeItem.texture '+getIMG_Normal().id+'')

# Set decals sources and materials
getMESH_Decals().select(replace=True)
lx.eval('select.itemHierarchy')
lx.eval('poly.setMaterial Decals {0.0 0.0 0.0} 1.0 0.04 true false false')

getBAKE_RO_Decals().select()
lx.eval('bakeItem.source {} type:1')
lx.eval('bakeItem.setAsSource 0 1 0')
lx.eval('bakeItem.setUV Texture')

lx.eval('select.drop item')