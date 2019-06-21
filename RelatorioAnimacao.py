import bpy

def AnimaLocRotDef(self, context):

    context = bpy.context
    scn = context.scene

    bpy.ops.anim.keyframe_insert_menu(type='BUILTIN_KSI_LocRot')


class AnimaLocRot(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "anim.ortog_loc_rot"
    bl_label = "Kinematic Ortog"
    
    def execute(self, context):
       AnimaLocRotDef(self, context)
       return {'FINISHED'}

bpy.utils.register_class(AnimaLocRot)
