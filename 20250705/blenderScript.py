# import python bpy
import bpy

# move cube down
bpy.ops.transform.translate(value=(-1.25085, -5.15893, -3.07553), 
orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), 
orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, 
proportional_edit_falloff='SMOOTH', proportional_size=1, 
use_proportional_connected=False, use_proportional_projected=False, 
snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, 
snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, 
use_snap_selectable=False)

# move cube back up
bpy.ops.transform.translate(value=(-1.25085, -5.15893, -3.07553), 
orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), 
orient_matrix_type='GLOBAL', constraint_axis=(True, True, True), mirror=False, 
use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, 
use_proportional_connected=False, use_proportional_projected=False, snap=False, 
snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', 
use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False)
  