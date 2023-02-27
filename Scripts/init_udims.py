# python

from definitions import *
import modo

# Configure the project for UDIMs

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
	getBAKE_RO_AO().select()
	getBAKE_RO_Seams().select()
	getBAKE_RO_ID().select()
	getBAKE_RO_ShadingNormal().select()
	getBAKE_RO_Decals().select()
	lx.eval('item.channel bakeItemRO$useUDIM true')
	lx.eval('item.channel bakeItemRO$startUDIM 1001')
	lx.eval('item.channel bakeItemRO$endUDIM '+rangeEnd+'')

rangeEnd = askRangeEnd()
setBakeUDIMs()
