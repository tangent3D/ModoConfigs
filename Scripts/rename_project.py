# python

import modo
from definitions import *

# Get project name from user
lx.eval("user.defNew name:UserValueProjectName type:string life:momentary")
lx.eval('user.def UserValueProjectName dialogname "Set project name"')
lx.eval("user.def UserValueProjectName username {Name}")

try:
    lx.eval("?user.value UserValueProjectName")
    userResponse = lx.eval("dialog.result ?")

except:
    userResponse = lx.eval("dialog.result ?")
    sys.exit()

projectName = lx.eval("user.value UserValueProjectName ?")

lx.out('Project name:',projectName)

# Rename mesh material mask to match project name
getMASK_MAT_LO().select(replace=True)
lx.eval("dialog.result ok")
lx.eval('texture.name "' + projectName + '"')

# Rename Mesh_LO to match project name
getMESH_LO().select(replace=True)
lx.eval('item.name "' + projectName + '"')

# Rename MESH_HI to match project name
getMESH_HI().select(replace=True)
lx.eval('item.name "' + projectName + '_HI"')

# Rename MESH_Decals to match project name
getMESH_Decals().select(replace=True)
lx.eval('item.name "' + projectName + '_Decals"')

# Rename render output file names with project name + suffix
getBAKE_RO_ShadingNormal().select(replace=True)
lx.eval('item.channel bakeItemRO$outPattern "' + projectName +'_World_Space_Normals"')

getBAKE_RO_Curvature().select(replace=True)
lx.eval('item.channel bakeItemRO$outPattern "' + projectName +'_Curvature"')

getBAKE_RO_AO().select(replace=True)
lx.eval('item.channel bakeItemRO$outPattern "' + projectName +'_Ambient_Occlusion"')

getBAKE_RO_Seams().select(replace=True)
lx.eval('item.channel bakeItemRO$outPattern "' + projectName +'_Seams"')

getBAKE_RO_ID().select(replace=True)
lx.eval('item.channel bakeItemRO$outPattern "' + projectName +'_ID"')

getBAKE_RO_Alpha().select(replace=True)
lx.eval('item.channel bakeItemRO$outPattern "' + projectName +'_Mask"')

getBAKE_RO_Decals().select(replace=True)
lx.eval('item.channel bakeItemRO$outPattern "' + projectName +'_Decals_ID"')

lx.eval('select.drop item')