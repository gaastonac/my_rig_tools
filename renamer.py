import maya.cmds as cmds
if cmds.window("Renamer",exists=True):
	cmds.deleteUI("Renamer")
window = cmds.window("Renamer", title="Renamer", iconName='Renamer',s=False, widthHeight=(390, 310) )
cmds.columnLayout( adjustableColumn=True )
cmds.separator( height=10, style='double' )
cmds.text ('Create by. Gaastonac')
cmds.separator( height=10, style='double' )
rename=cmds.textFieldGrp(l="rename", editable=True)
cmds.button( label='Put', command=('add()'))
cmds.showWindow( window )

def add():
    obj_to_rename=cmds.textFieldGrp(rename, q=True,text=True)
    print obj_to_rename
    num=0
    for i in cmds.ls(sl=True):
        cmds.rename(i,obj_to_rename+'_'+str(num).zfill(2))
        num=num+1
