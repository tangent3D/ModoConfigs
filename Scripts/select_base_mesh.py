# python
import modo
import lx

items = modo.Scene().selected
for item in items:
	if item.type == 'mesh':
		lx.eval('deformer.SelectBaseMesh select:?+')