# python

from definitions import *

lx.eval('select.drop item')
lx.eval('shader.setVisible '+ TEX_Curvature +' false')
lx.eval('select.subItem '+ BAKE_TEX_Normal +' set')
lx.eval('bakeItem.bake true')
lx.eval('shader.setVisible '+ TEX_Curvature +' true')
lx.eval('select.drop item')

lx.eval('shader.setVisible '+IMG_Normal+' true')

# Reload the normal map image to update it in the viewport
lx.eval('select.subItem '+MESH_LO+'')
name = lx.eval('item.name ?')
lx.eval('select.subItem {'+name+'_Normal_Base:videoStill001} set mediaClip')
lx.eval('clip.reload')
lx.eval('select.drop item')