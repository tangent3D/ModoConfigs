# python

from definitions import *

# Creating normal maps and configuring the project for UDIMs

def createNormalsDefault():
	# Make a single normal map image and parent it in the MESH_LO material
	lx.eval('clip.newStill "' +getOutputDir()+ '\\' +getProjectName()+ '_Normal_Base.png" x2048 RGB false false {0.0 0.0 0.0} PNG (none)')
	lx.eval('select.subItem {' + getProjectName() + '_Normal_Base:videoStill001} set mediaClip')
	lx.eval('texture.new clip:{' + getProjectName() +'_Normal_Base:videoStill001}')
	getMASK_MAT_LO().select()
	lx.eval('texture.parent '+getMASK_MAT_LO().id+'')
	lx.eval('select.subItem '+getMASK_MAT_LO().id+' remove')
	lx.eval('item.channel textureLayer(txtrLocator)$projType uv')
	lx.eval('texture.setUV Texture')
	lx.eval('shader.setEffect normal')
	# While texture layer is selected, assign normal texture output to TS normal bake item
	getBAKE_TEX_Normal().select()
	lx.eval('bakeItem.texture {}')
	lx.eval('bakeItem.setAsTextureOutput 0')
	lx.eval('select.drop item')

def createNormalsUDIMs():
	getMASK_MAT_LO().select(replace=True)
	lx.eval('clip.udimWizard "'+getOutputDir()+'" '+getProjectName()+'_Normal_Base '+rangeStart+' '+rangeEnd+' x2048 rgb false false format:PNG overwrite:true')
	lx.eval('shader.create imageMap 0')
	# Set TS Normal image map folder effect to Normal while it's selected
	lx.eval('item.channel textureLayer(txtrLocator)$projType uv')
	lx.eval('texture.setUV Texture')
	lx.eval('shader.setEffect normal')

def askUDIMs():
	# Check if the project should be configured for UDIMs
	return modo.dialogs.yesNo('UDIMs','Use UDIMs?')

def askRangeStart():
	#Get desired UDIM range start from user
	lx.eval("user.defNew name:UserValueRangeStart type:string life:momentary")
	lx.eval('user.def UserValueRangeStart dialogname "Set UDIM Range Start"')
	lx.eval("user.def UserValueRangeStart username {Default: 1001}")

	try:
		lx.eval("?user.value UserValueRangeStart")
		userResponse = lx.eval("dialog.result ?")
	except:
		pass

	rangeStart = lx.eval("user.value UserValueRangeStart ?")

	if rangeStart == "":
		rangeStart = "1001"

	return rangeStart

def askRangeEnd():
	#Get desired UDIM range end from user
	lx.eval("user.defNew name:UserValueRangeEnd type:string life:momentary")
	lx.eval('user.def UserValueRangeEnd dialogname "Set UDIM Range End"')
	lx.eval("user.def UserValueRangeEnd username {Default: 1001}")

	try:
		lx.eval("?user.value UserValueRangeEnd")
		userResponse = lx.eval("dialog.result ?")
	except:
		pass

	rangeEnd = lx.eval("user.value UserValueRangeEnd ?")

	if rangeEnd == "":
		rangeEnd = "1001"

	return rangeEnd

def setBakeUDIMs():
	getBAKE_RO_Alpha().select(replace=True)
	getBAKE_RO_Curvature().select()
	getBAKE_RO_ID().select()
	getBAKE_RO_ShadingNormal().select()
	getBAKE_RO_Decals().select()
	lx.eval('item.channel bakeItemRO$useUDIM true')
	lx.eval('item.channel bakeItemRO$startUDIM '+rangeStart+'')
	lx.eval('item.channel bakeItemRO$endUDIM '+rangeEnd+'')

try:
	getIMG_Normal().select(replace=True)
	lx.eval('texture.delete')
except:
	pass

if askUDIMs() == "yes":
	rangeStart = askRangeStart()
	rangeEnd = askRangeEnd()
	createNormalsUDIMs()
	setBakeUDIMs()
else:
	createNormalsDefault()

# Clean up any unused clips!
lx.eval('clip.purge')