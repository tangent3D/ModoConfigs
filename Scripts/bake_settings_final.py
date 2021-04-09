# python

from definitions import *

TEX_Curvature = getTEX_Curvature() 
BAKE_RO_ShadingNormal = getBAKE_RO_ShadingNormal()
BAKE_RO_Curvature = getBAKE_RO_Curvature()
BAKE_RO_Alpha = getBAKE_RO_Alpha()
BAKE_RO_ID = getBAKE_RO_ID()
BAKE_RO_Decals = getBAKE_RO_Decals()

TEX_Curvature.select(replace=True)
lx.eval('item.channel occlusion$rays 32')

BAKE_RO_ShadingNormal.select(replace=True)
BAKE_RO_ShadingNormal.select()
BAKE_RO_Curvature.select()
BAKE_RO_Alpha.select()
BAKE_RO_ID.select()
BAKE_RO_Decals.select()

lx.eval('item.channel bakeItemRO$width 2048')
lx.eval('item.channel bakeItemRO$height 2048')

lx.eval('select.drop item')