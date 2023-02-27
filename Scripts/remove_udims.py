# python

from definitions import *
import modo

getBAKE_RO_Alpha().select(replace=True)
getBAKE_RO_Curvature().select()
getBAKE_RO_AO().select()
getBAKE_RO_Seams().select()
getBAKE_RO_ID().select()
getBAKE_RO_ShadingNormal().select()
getBAKE_RO_Decals().select()
lx.eval('item.channel bakeItemRO$startUDIM 1001')
lx.eval('item.channel bakeItemRO$endUDIM 1001')
lx.eval('item.channel bakeItemRO$useUDIM false')