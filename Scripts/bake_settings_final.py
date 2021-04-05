# python

from definitions import *

lx.eval('select.drop item')

lx.eval('select.subItem '+ TEX_Curvature +'')
lx.eval('item.channel occlusion$rays 32')
lx.eval('select.subItem '+ RO_AO +'')
lx.eval('item.channel renderOutput$occlRays 32')

lx.eval('select.subItem ' + BAKE_RO_ShadingNormal + '')
lx.eval('select.subItem ' + BAKE_RO_Curvature + '')
lx.eval('select.subItem ' + BAKE_RO_Alpha + '')
lx.eval('select.subItem ' + BAKE_RO_AO + '')
lx.eval('select.subItem ' + BAKE_RO_ID + '')
lx.eval('select.subItem ' + BAKE_RO_Decals + '')


lx.eval('item.channel bakeItemRO$width 2048')
lx.eval('item.channel bakeItemRO$height 2048')

lx.eval('select.drop item')