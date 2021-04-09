# python

import modo

def getProjectName():
	x = modo.item.Item('locator.LO').parent
	return x.name

def getMESH_LO():
	return modo.item.Item('locator.LO').parent

def getMESH_HI():
	return modo.item.Item('locator.HI').parent

def getMESH_Decals():
	return modo.item.Item('locator.Decals').parent

def getMASK_MAT_LO():
	x = modo.item.Item('locator.LO').parent
	return modo.item.Item(''+x.name+' (Material)')

def getMAT_LO():
	x = modo.item.Item('locator.LO').parent
	y = modo.item.Item(''+x.name+' (Material)')
	z = y.childrenByType('advancedMaterial')
	return z[0]
	
def getMASK_MAT_RoundEdge():
	return modo.item.Item('RoundEdge (Material)')

def getMAT_RoundEdge():
	x = modo.item.Item('RoundEdge (Material)')
	y = x.childrenByType('advancedMaterial')
	return y[0]

def getRO_Alpha():
	return modo.item.Item('Alpha Output')

def getRO_Diffuse():
	return modo.item.Item('Diffuse Color Output')

def getRO_ShadingNormal():
	return modo.item.Item('Shading Normal Output')

def getRO_ID():
	return modo.item.Item('Surface ID Output')	

def getTEX_Curvature():
	return modo.item.Item('Curvature')
							
def getTEX_Wireframe():
	return modo.item.Item('Wireframe Texture')

def getBAKE_RO_ShadingNormal():
	return modo.item.Item('World Space Normals Bake')

def getBAKE_RO_Curvature():
	return modo.item.Item('Curvature Bake')

def getBAKE_RO_Alpha():
	return modo.item.Item('Alpha Mask Bake')

def getBAKE_RO_ID():
	return modo.item.Item('Surface ID Bake')

def getBAKE_RO_Decals():
	return modo.item.Item('Decals ID Bake')

def getBAKE_TEX_Normal():
	return modo.item.Item('Tangent Space Normals Texture Bake')

def getIMG_Normal():
	x = modo.item.Item('locator.LO').parent
	return modo.item.Item(''+x.name+'_Normal_Base (Image)')