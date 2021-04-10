# python

from definitions import *

getTEX_Curvature().select(replace=True)
lx.eval('item.channel occlusion$rays 1')

getBAKE_RO_ShadingNormal().select(replace=True)
getBAKE_RO_ShadingNormal().select()
getBAKE_RO_Curvature().select()
getBAKE_RO_Alpha().select()
getBAKE_RO_ID().select()
getBAKE_RO_Decals().select()

lx.eval('item.channel bakeItemRO$width 1024')
lx.eval('item.channel bakeItemRO$height 1024')

lx.eval('select.drop item')