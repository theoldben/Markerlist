import bpy

class MarkerList(bpy.types.Operator):
    """Timeline Markers list"""
    bl_idname = "marker.list"
    bl_label = "Marker List"

    @classmethod
    def poll(cls, context):
        return context.scene.timeline_markers
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        return {'FINISHED'}

def marker_list_function(self, context):
    self.layout.operator('marker.list')
