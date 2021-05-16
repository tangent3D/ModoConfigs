# python

from definitions import *

lx.eval('select.drop item')

### Set HI Sources ###

# Assign RoundEdge material to HP mesh and all children
getMESH_HI().select(replace=True)
lx.eval('select.itemHierarchy')
lx.eval('poly.setMaterial RoundEdge {1.0 1.0 1.0} 1.0 0.04 true false false')

# Assign HI Sources to Render Output Bake Items
getBAKE_RO_ShadingNormal().select()
getBAKE_RO_Curvature().select()
getBAKE_RO_Seams().select()
getBAKE_RO_Alpha().select()
getBAKE_RO_ID().select()

try:
	# Remove selected items as sources
	lx.eval('bakeItem.setAsSource 2 1 0')
except:
	pass

try:
	# Add selected items as sources
	lx.eval('bakeItem.setAsSource 1 1 0')
except:
	pass

print ("set ro bake item sources")

# Assign HI Sources to Texture Output Bake Items
getMESH_HI().select(replace=True)
lx.eval('select.itemHierarchy')
getBAKE_TEX_Normal().select()

try:
	# Removed selected items as sources
	lx.eval('bakeItem.setAsSource 2 0 0')
except:
	pass

try:
	# Add selected items as sources
	lx.eval('bakeItem.setAsSource 1 0 0')
except:
	pass

print ("set texture bake item sources")

### Set LO Targets ###

# Assign LO material to LO mesh and all children
getMESH_LO().select(replace=True)
name = lx.eval('item.name ?')
lx.eval('select.itemHierarchy')
lx.eval('poly.setMaterial '+name+' {1.0 1.0 1.0} 1.0 0.04 true false')

# Assign LO + Decals Targets to Render Output Bake Items

getBAKE_RO_ShadingNormal().select()
getBAKE_RO_Seams().select()
getBAKE_RO_Curvature().select()
getBAKE_RO_Alpha().select()
getBAKE_RO_ID().select()
getBAKE_RO_Decals().select()

try:
	# Remove selected items as targets
	lx.eval('bakeItem.setAsTarget 2 1 0')
except:
	pass

try:
	# Add selected items as targets
	lx.eval('bakeItem.setAsTarget 1 1 0')
except:
	pass

print("set ro bake item targets")

# Assign LO Targets to Texture Output Bake Items

getMESH_LO().select(replace=True)
lx.eval('select.itemHierarchy')

getBAKE_TEX_Normal().select()
lx.eval('bakeItem.texture '+getIMG_Normal().id+'')

try:
	# Remove selected items as targets
	lx.eval('bakeItem.setAsTarget 2 0 0')
except:
	pass

try:
	# Add selected items as targets
	lx.eval('bakeItem.setAsTarget 1 0 0')
except:
	pass

print("set texture bake item targets")

### Set Decals Sources ###

# Assign Decals material to Decals mesh and all children
getMESH_Decals().select(replace=True)
lx.eval('select.itemHierarchy')
lx.eval('poly.setMaterial Decals {0.0 0.0 0.0} 1.0 0.04 true false false')

getBAKE_RO_Decals().select()

try:
	# Remove selected items as sources
	lx.eval('bakeItem.setAsSource 2 1 0')
except:
	pass

try:
	# Add selected items as sources
	lx.eval('bakeItem.setAsSource 1 1 0')
except:
	pass

print("set decals render output bake item targets")

lx.eval('select.drop item')