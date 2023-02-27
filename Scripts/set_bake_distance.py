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

# Set bake distance on render output bake items
getBAKE_RO_ShadingNormal().select(replace=True)
getBAKE_RO_Curvature().select()
getBAKE_RO_AO().select()
getBAKE_RO_Seams().select()
getBAKE_RO_Alpha().select()
getBAKE_RO_ID().select()
getBAKE_RO_Decals().select()
lx.eval('item.channel bakeItemRO$distance '+ user_input +'')

lx.eval('select.drop item')
