#python
import modo
from definitions import *

try:
	lx.eval('select.vertexMap Cage morf replace')
except:
	getMESH_LO().select(replace=True)
	lx.eval('select.itemHierarchy')
	lx.eval('vertmap.new Cage morf')

getBAKE_RO_ShadingNormal().select(replace=True)
getBAKE_RO_Curvature().select()
getBAKE_RO_AO().select()
getBAKE_RO_Seams().select()
getBAKE_RO_Alpha().select()
getBAKE_RO_ID().select()
getBAKE_RO_Decals().select()
lx.eval('bakeItem.setCage Cage render')

lx.eval('select.drop item')
