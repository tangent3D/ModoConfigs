# python

import modo
from definitions import *

getBAKE_RO_Alpha().select(replace=True)
getBAKE_RO_Curvature().select()
getBAKE_RO_AO().select()
getBAKE_RO_Seams().select()
getBAKE_RO_ID().select()
getBAKE_RO_ShadingNormal().select()
getBAKE_RO_Decals().select()
lx.eval('item.channel bakeItemRO$width 512')
lx.eval('item.channel bakeItemRO$height 512')