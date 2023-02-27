# python

import modo
from definitions import *

# Set render output directory (usually project's 'bake' folder)
lx.eval('dialog.setup dir')
lx.eval('dialog.title "Set project bake directory"')
lx.eval('dialog.result "D:\Dropbox"')
lx.eval('dialog.open')
output_dir = lx.eval('dialog.result ?')

# Set output directory on Render Output Bake Items
getBAKE_RO_Alpha().select(replace=True)
getBAKE_RO_Curvature().select()
getBAKE_RO_AO().select()
getBAKE_RO_Seams().select()
getBAKE_RO_ID().select()
getBAKE_RO_ShadingNormal().select()
getBAKE_RO_Decals().select()
lx.eval('item.channel outLocation "' + output_dir + '"')
