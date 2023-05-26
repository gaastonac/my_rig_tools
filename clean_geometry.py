import maya.cmds as cmds
if  cmds.window('Clean_Tool',exists = True):
    cmds.deleteUI('Clean_Tool')
window = cmds.window('Clean_Tool', title="Clean", iconName='Short Name',s=False, widthHeight=(200, 125) )
cmds.columnLayout( adjustableColumn=True )
cmds.separator( height=10, style='double' )
cmds.text ('Created by. Gaastonac',bgc=[1,1,0],fn="obliqueLabelFont",w=5)
cmds.separator( height=10, style='double' )
cmds.button( label='CLEAN',command=('CLEAN()'),h=40)
cmds.separator( height=5, style='double' )
cmds.rowColumnLayout(numberOfColumns=3, columnWidth=[ (1,70),(2,70),(3,70)], columnOffset=[(4,'right',3)])
Freeze=cmds.checkBox(label='Freeze')
History=cmds.checkBox(label='History')
Pivot=cmds.checkBox(label='Pivot')
Text_Vacio=cmds.text( label='' )
All=cmds.checkBox(label='ALL',w=1,h=30)
Text_Vacio=cmds.text( label='' )
cmds.showWindow( window )
def CLEAN():
    Selected_Geometry = cmds.ls (type='transform')
    print Selected_Geometry
    List_Objects_Deselect=['persp','top','front','side']
    for Object in List_Objects_Deselect:
        if cmds.objExists(Object):
          Selected_Geometry.remove(Object)
    print Selected_Geometry
    for Obj in Selected_Geometry:
        checkboxAll= cmds.checkBox(All, q=True, v=True)
        checkboxFreeze= cmds.checkBox(Freeze, q=True, v=True)
        checkboxPivot= cmds.checkBox(Pivot, q=True, v=True)
        checkboxHistory= cmds.checkBox(History, q=True, v=True)
        if checkboxAll==True:
            cmds.makeIdentity(Obj,apply=True, t=1, r=1, s=1, n=0 )
            cmds.delete(Obj,ch=True)
            cmds.move(0,0,0,Obj+'.scalePivot',Obj+'.rotatePivot',rpr=True)
        if checkboxFreeze==True:
            cmds.makeIdentity(Obj,apply=True, t=1, r=1, s=1, n=0 )
        if checkboxPivot==True:
            cmds.move(0,0,0,Obj+'.scalePivot',Obj+'.rotatePivot',rpr=True)
        if checkboxHistory==True:
            cmds.delete(Obj,ch=True)