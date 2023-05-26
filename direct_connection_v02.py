import maya.cmds as cmds

if cmds.window("Direct Connection", exists=True):
    cmds.deleteUI("Direct Connection")
window = cmds.window("Direct Connection"
                     , title="Direct Connection"
                     , iconName='Direct Connection'
                     , s=False
                     ,widthHeight=(390, 310))
cmds.columnLayout(adjustableColumn=True)
cmds.separator(height=10, style='double')
cmds.text('Create by. Gaastonac')
cmds.separator(height=10, style='double')
cmds.button( label='Conect', command=('connection()'),h=50)
def input_Object(txt_btn_grp_input):  # Define parameter for the `textFieldButtonGrp`
    global name_input
    # Get selection.
    sel = cmds.ls(sl=True)
    if not sel:
        cmds.warning("No objects are selected!")
    else:
        obj_input=cmds.textFieldButtonGrp(txt_btn_grp_input, edit=True, tx=','.join(sel), buttonLabel='OK'
                                , backgroundColor=(.5, .8, .2))
        name_input=cmds.textFieldGrp(obj_input, q=1, text=True)

#Create textFieldButtonGrp
obj_input_button = cmds.textFieldButtonGrp(editable=False, adj=True, buttonLabel='Input')

# Now define the function with its variable.
cmds.textFieldButtonGrp(obj_input_button, e=True, bc='input_Object(obj_input_button)')

def target_Object(txt_btn_grp_target):  # Define parameter for the `textFieldButtonGrp`
    global name_target
    # Get selection.
    sel = cmds.ls(sl=True)
    if not sel:
        cmds.warning("No objects are selected!")
    else:
        obj_target=cmds.textFieldButtonGrp(txt_btn_grp_target, edit=True, tx=','.join(sel), buttonLabel='OK'
                                , backgroundColor=(.5, .8, .2))
        name_target=cmds.textFieldGrp(obj_target, q=1, text=True)

obj_target_button = cmds.textFieldButtonGrp(editable=False, adj=True, buttonLabel='Target')

# Now define the function with its variable.
cmds.textFieldButtonGrp(obj_target_button, e=True, bc='target_Object(obj_target_button)')

def connection():
    print name_input +'  and   ' + name_target +'     se conectaran dependiendo del atributo '



cmds.showWindow(window)
