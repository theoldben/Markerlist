import bpy

class SCENE_PT_MarkerList(bpy.types.Panel):
    """Timeline Markers list"""
    bl_idname = "SCENE_PT_MarkerList"
    bl_label = "Marker List"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"

    def draw(self, context):
        scn = context.scene
        tool_settings = scn.tool_settings
        marker_list = scn.timeline_markers
        layout = self.layout
        
        col = layout.column(align=True)
        if scn.tool_settings.lock_markers: col.enabled = False
        else: col.enabled = True
            
        for k, marker in sorted(marker_list.items(), key=lambda it:it[1].frame):
            row = col.row(align=True)
            # go to frame
            if scn.frame_current == marker.frame: icon='RADIOBUT_ON'
            else: icon='RADIOBUT_OFF'
            op = row.operator('marker.go_to', text='', icon=icon, emboss=False)
            op.frame = marker.frame
            # name
            row.prop(marker, "name", text="")
            # selection
            if marker.select: icon = 'RESTRICT_SELECT_OFF'
            else: icon = 'RESTRICT_SELECT_ON'
            row.prop(marker, "select", text="", icon=icon)
            # frame
            row.prop(marker, "frame", text="")
            
            # delete
            op = row.operator('marker.remove', text='', icon='X')
            op.frame = marker.frame
            # camera
            if marker.camera: icon = 'VIEW_CAMERA'
            else: icon = 'CAMERA_DATA'
            row.label(text="", icon=icon)
            
        row = layout.row(align=True)
        row.prop(scn, 'frame_current', text='Frame')
        row.separator()
        op = row.operator('screen.marker_jump', text='', icon='TRIA_LEFT')
        op.next = False
        op = row.operator('screen.marker_jump', text='', icon='TRIA_RIGHT')
        op.next = True
        row.separator()
        if tool_settings.lock_markers: icon='LOCKED'
        else: icon='UNLOCKED'
        row.prop(tool_settings, 'lock_markers', text='', icon=icon)
        row.separator()
        row.operator('marker.remove_selected', text='Selected', icon='X')
        