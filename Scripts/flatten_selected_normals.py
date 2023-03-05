# python

import modo

try:
	lx.eval('select.vertexMap "Vertex Normal" norm add')

except RuntimeError:
	modo.dialogs.alert('Error', 'Create a vertex normal map first.', dtype='error')
	sys.exit(1)

try:
	lx.eval('workPlane.fitSelect')
	lx.eval('tool.set TransformNormals on')
	lx.eval('tool.noChange')
	lx.eval('tool.attr xfrm.transform TY 100.0')
	lx.eval('tool.doApply')
	lx.eval('select.nextMode')
	lx.eval('workPlane.state false')
except RuntimeError:
	modo.dialogs.alert('Error', 'Failed.', dtype='error')
	sys.exit(1)
