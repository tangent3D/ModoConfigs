# python

from definitions import *

# Assign RoundEdge material to selected items
lx.eval('poly.setMaterial RoundEdge {0.8 0.8 0.8} 1.0 0.04 true false false')

lx.eval('select.subitem ' + BAKE_TEX_Normal + ' remove')
lx.eval('select.subitem ' + BAKE_TEX_Displacement + ' remove')

lx.eval('select.subItem ' + BAKE_RO_ShadingNormal + ' set')
lx.eval('select.subItem ' + BAKE_RO_Curvature + ' set')
lx.eval('select.subItem ' + BAKE_RO_Alpha + ' set')
lx.eval('select.subItem ' + BAKE_RO_AO + ' set')
lx.eval('select.subItem ' + BAKE_RO_ID + ' set')

lx.eval('bakeItem.source {} type:1')
lx.eval('bakeItem.setAsSource 0 1 0')
lx.eval('bakeItem.setUV Texture')

lx.eval('select.subItem ' + BAKE_RO_ShadingNormal + ' remove')
lx.eval('select.subItem ' + BAKE_RO_Curvature + ' remove')
lx.eval('select.subItem ' + BAKE_RO_Alpha + ' remove')
lx.eval('select.subItem ' + BAKE_RO_AO + ' remove')
lx.eval('select.subItem ' + BAKE_RO_ID + ' remove')

lx.eval('select.subitem ' + BAKE_TEX_Normal + ' set')
lx.eval('select.subitem ' + BAKE_TEX_Displacement + ' set')

lx.eval('bakeItem.source {} type:0')
lx.eval('bakeItem.setAsSource 0 0 0')

lx.eval('select.drop item')