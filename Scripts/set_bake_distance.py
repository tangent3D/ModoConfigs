# python

from definitions import *

BAKE_RO_ShadingNormal = getBAKE_RO_ShadingNormal()
BAKE_RO_Curvature = getBAKE_RO_Curvature()
BAKE_RO_Alpha = getBAKE_RO_Alpha()
BAKE_RO_ID = getBAKE_RO_ID()
BAKE_RO_Decals = getBAKE_RO_Decals()
BAKE_TEX_Normal = getBAKE_TEX_Normal()

# Get desired bake distance from user
lx.eval("user.defNew name:UserValue type:string life:momentary")
lx.eval('user.def UserValue dialogname "Set bake distance"')
lx.eval("user.def UserValue username {Bake distance (meters)}")

try:
    lx.eval("?user.value UserValue")
    userResponse = lx.eval("dialog.result ?")
    
except:
    userResponse = lx.eval("dialog.result ?")
    sys.exit()
    
user_input = lx.eval("user.value UserValue ?")
lx.out('Bake distance:',user_input)

# Set bake distance on render output bake items
BAKE_RO_ShadingNormal.select(replace=True)
BAKE_RO_Curvature.select()
BAKE_RO_Alpha.select()
BAKE_RO_ID.select()
BAKE_RO_Decals.select()
lx.eval('item.channel bakeItemRO$distance '+ user_input +'')

# Set bake distance on texture bake items
BAKE_TEX_Normal.select(replace=True)
lx.eval('item.channel bakeItemTexture$distance '+ user_input +'')
lx.eval('select.drop item')