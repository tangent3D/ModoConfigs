# python

from definitions import *

# Get desired round edge width from user
lx.eval("user.defNew name:UserValue type:string life:momentary")
lx.eval('user.def UserValue dialogname "Set round edge width"')
lx.eval("user.def UserValue username {Round edge width (meters)}")

try:
    lx.eval("?user.value UserValue")
    userResponse = lx.eval("dialog.result ?")
    
except:
    userResponse = lx.eval("dialog.result ?")
    sys.exit()
    
user_input = lx.eval("user.value UserValue ?")
lx.out('Round edge width:',user_input)

# Set RoundEdge material width
getMAT_RoundEdge().select(replace=True)
lx.eval('item.channel advancedMaterial$rndWidth '+ user_input +'')

# Set Curvature Occlusion Distance to RE width * 10
occlusionDistance = float(user_input)
occlusionDistance = (occlusionDistance * 10)
occlusionDistance = str(occlusionDistance)
getTEX_Curvature().select(replace=True)
lx.eval('item.channel occlusion$dist ' + occlusionDistance + '')

# Set Wireframe Texture line width to RE width / 2
lineWidth = float(user_input)
lineWidth = (lineWidth / 2)
lineWidth = str(lineWidth)
getTEX_Wireframe().select(replace=True)
lx.eval('item.channel val.wireframe$width '+ lineWidth +'')

lx.eval('select.drop item')