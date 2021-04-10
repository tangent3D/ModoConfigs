# python

from definitions import *

getTEX_Curvature().select(replace=True)
lx.eval('item.channel occlusion$rays 32')

getBAKE_RO_ShadingNormal().select(replace=True)
getBAKE_RO_ShadingNormal().select()
getBAKE_RO_Curvature().select()
getBAKE_RO_Alpha().select()
getBAKE_RO_ID().select()
getBAKE_RO_Decals().select()

lx.eval('item.channel bakeItemRO$width 2048')
lx.eval('item.channel bakeItemRO$height 2048')

lx.eval('select.drop item')