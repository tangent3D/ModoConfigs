# python

from definitions import *

# Clean UV maps from HI and Decal meshes
lx.eval('@clean_uv_maps.py')

# Clean all sources/targets
lx.eval('@clean_sources_targets.py')

# Assign HI, LO, Decals materials
lx.eval('@set_materials.py')

### Set HI Sources ###

getMESH_HI().select(replace=True)
lx.eval('select.itemHierarchy')

# Assign HI Sources to Render Output Bake Items
getBAKE_RO_ShadingNormal().select()
getBAKE_RO_Curvature().select()
getBAKE_RO_AO().select()
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

### Set LO Targets ###

# Assign LO Targets to Render Output Bake Items
getMESH_LO().select(replace=True)
lx.eval('select.itemHierarchy')

getBAKE_RO_ShadingNormal().select()
getBAKE_RO_Seams().select()
getBAKE_RO_Curvature().select()
getBAKE_RO_AO().select()
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

### Set Decals Sources ###

getMESH_Decals().select(replace=True)
lx.eval('select.itemHierarchy')

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

lx.eval('select.drop item')
