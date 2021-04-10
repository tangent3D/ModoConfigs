# python

import modo

scene = modo.Scene()

try:
	# Roughly check if scene has already been initialized
	scene.item('locator.LO').select()
	modo.dialogs.alert('Scene already initialized', 'Please create a new scene first.', dtype='info')
except:
	# Proceed with initializing the project
	lx.eval('@init_scene.py')
	lx.eval('@init_normals_udims.py')
	# Finish up
	lx.eval('@set_sources_targets.py')
	lx.eval('@show_HI.py')