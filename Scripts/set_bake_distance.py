# python

from definitions import *

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

# Select render output bake items
lx.eval('select.drop item')
lx.eval('select.subItem ' + BAKE_RO_ShadingNormal + '')
lx.eval('select.subItem ' + BAKE_RO_Curvature + '')
lx.eval('select.subItem ' + BAKE_RO_Alpha + '')
lx.eval('select.subItem ' + BAKE_RO_AO + '')
lx.eval('select.subItem ' + BAKE_RO_ID + '')

# Set bake distance on render output bake items
lx.eval('item.channel bakeItemRO$distance '+ user_input +'')
lx.eval('select.drop item')

# Set bake distance on texture bake items
lx.eval('select.subItem ' + BAKE_TEX_Normal + '')
lx.eval('select.subItem ' + BAKE_TEX_Displacement + '')

# Set bake distance on texture bake items
lx.eval('item.channel bakeItemTexture$distance '+ user_input +'')
lx.eval('select.drop item')