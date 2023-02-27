# python

import modo
from definitions import *

getBAKE_RO_Alpha().select(replace=True)
getBAKE_RO_Curvature().select()
getBAKE_RO_AO().select()
getBAKE_RO_Seams().select()
getBAKE_RO_ID().select()
getBAKE_RO_ShadingNormal().select()
lx.eval('item.channel bakeItemRO$width 2048')
lx.eval('item.channel bakeItemRO$height 2048')

getBAKE_RO_Decals().select(replace=True)
lx.eval('item.channel bakeItemRO$width 4096')
lx.eval('item.channel bakeItemRO$height 4096')
