import maya.cmds as cmds

# Make a new window

if cmds.window('j_vis',exists=True):
    
    cmds.deleteUI('j_vis')
    
window = cmds.window('j_vis',title='j_vis', iconName='Short Name',s=False, widthHeight=(180, 120) )

cmds.columnLayout( adjustableColumn=True )

cmds.separator( height=10, style='double' )

cmds.text ('Create by. Gaastonac')

cmds.separator( height=10, style='double' )

cmds.button( label='Visibility On', command=('on()'),h=40)

cmds.button( label='Visibility Off', command=('off()'),h=40)

cmds.showWindow( window )

def on():
    
    joints = cmds.ls(type='joint')
    
    for joint in joints:
        
        cmds.setAttr('{}.drawStyle'.format(joint),2)
        
def off():
    
    joints = cmds.ls (type='joint')
    
    for joint in joints:
        
        cmds.setAttr('{}.drawStyle'.format(joint),0)