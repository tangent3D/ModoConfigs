# python

from definitions import *

lx.eval('shader.setVisible '+ TEX_Curvature +' false')

lx.eval('select.drop item')

lx.eval('select.subItem '+ BAKE_RO_AO +' set')

lx.eval('pref.value render.bakeBorder 0')
lx.eval('bakeItem.bake true')
lx.eval('pref.value render.bakeBorder 16')

lx.eval('shader.setVisible '+ TEX_Curvature +' true')

lx.eval('select.drop item')