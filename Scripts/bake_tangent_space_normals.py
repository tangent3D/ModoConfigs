# python

from definitions import *

lx.eval('shader.setVisible '+ TEX_Curvature +' false')

lx.eval('select.drop item')

lx.eval('select.subItem '+ BAKE_TEX_Normal +' set')

lx.eval('bakeItem.bake true')

lx.eval('shader.setVisible '+ TEX_Curvature +' true')

# Set the Normal image layer visible to I can see how the bake turned out!
lx.eval('shader.setVisible '+ IMG_Normal +' true')

lx.eval('select.drop item')