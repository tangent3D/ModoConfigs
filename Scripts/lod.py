# python
import modo
import lx
import fnmatch
import traceback
from show import showLow

def main():
	args = lx.args()
	for arg in args:
		if arg == 'LOD1':
			lx.eval('view3d.enableDeformers true')
			disableLOD()
			enableLOD("LOD1")
			
		if arg == 'LOD2':
			lx.eval('view3d.enableDeformers true')
			disableLOD()
			enableLOD("LOD1")
			enableLOD("LOD2")
			
		if arg == 'LOD3':
			lx.eval('view3d.enableDeformers true')
			disableLOD()
			enableLOD("LOD1")
			enableLOD("LOD2")
			enableLOD("LOD3")
			
        if arg == 'disable':
			lx.eval('view3d.enableDeformers false')
			showLow()
			lx.eval('@select_base_mesh.py')
			disableLOD()

# select LOD mesh ops (delete, poly reduction) by name (e.g. "LOD1") and enable/disable them with bool
def enableLOD(name):
	lx.eval('select.drop item')
	
	for item in modo.Scene().items():	
		if fnmatch.fnmatch(item.name, name + "*") and item.type == "delete.meshop.item" or item.type == "poly.reduct.item":
			modo.Scene().select(item, add=True)
			lx.eval('item.channel meshoperation$enable true')
				
	# except if no matching LOD mesh ops found	
	if modo.Scene().selected == []:
		print("No matching LOD mesh ops found.")
		raise Exception

# disable all LOD mesh ops
def disableLOD():	
	for item in modo.Scene().items():	
		if fnmatch.fnmatch(item.name, "LOD*") and item.type == "delete.meshop.item" or item.type == "poly.reduct.item":
			modo.Scene().select(item, add=True)
			lx.eval('item.channel meshoperation$enable false')
				
	# except if no LOD mesh ops found	
	if modo.Scene().selected == []:
		print("No LOD mesh ops found.")
		raise Exception
        
if __name__ == '__main__':
   try:
      main()
   except:
      lx.out(traceback.format_exc())