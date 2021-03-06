# python

from definitions import *

lx.eval('shader.setVisible '+ TEX_Curvature +' true')

lx.eval('select.drop item')

lx.eval('select.subItem '+ BAKE_RO_Curvature +' set')

lx.eval('bakeItem.bake true')

lx.eval('select.drop item')