# python

from definitions import *

lx.eval('select.drop item')

lx.eval('select.subItem '+ TEX_Curvature +'')
lx.eval('item.channel occlusion$rays 1')
lx.eval('select.subItem '+ RO_AO +'')
lx.eval('item.channel renderOutput$occlRays 1')

lx.eval('select.subItem ' + BAKE_RO_ShadingNormal + '')
lx.eval('select.subItem ' + BAKE_RO_Curvature + '')
lx.eval('select.subItem ' + BAKE_RO_Alpha + '')
lx.eval('select.subItem ' + BAKE_RO_AO + '')
lx.eval('select.subItem ' + BAKE_RO_ID + '')

lx.eval('item.channel bakeItemRO$width 1024')
lx.eval('item.channel bakeItemRO$height 1024')

lx.eval('select.drop item')