# python

from definitions import *

# Remove all items as sources/targets from Render Output Bake Items
lx.eval('select.all')
getBAKE_RO_ShadingNormal().select()
getBAKE_RO_Seams().select()
getBAKE_RO_Curvature().select()
getBAKE_RO_AO().select()
getBAKE_RO_Alpha().select()
getBAKE_RO_ID().select()
getBAKE_RO_Decals().select()

try:
	# Remove selected items as sources
	lx.eval('bakeItem.setAsSource 2 1 0')
except:
	pass

try:
	# Remove selected items as targets
	lx.eval('bakeItem.setAsTarget 2 1 0')
except:
	pass

lx.eval('select.drop item')
