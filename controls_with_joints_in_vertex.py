import maya.cmds as cmds
sel=cmds.ls(selection=True,fl=True)
lsel=len(sel)
name=sel[0]
print name
NewName=name.split('.')[0]
print NewName

# Create a custom progressBar in a windows ...
window = cmds.window()
cmds.columnLayout()

if lsel>1:
    progressControl = cmds.progressBar(maxValue=lsel-1, width=300)
    
    cmds.showWindow( window )
num=0
for vertex in range(lsel):
    position= cmds.xform(sel[vertex], ws=True, q=True, t=True)

    orientation= cmds.xform(sel[vertex], ws=True, q=True, ro=True)
    vertex=cmds.xform(sel[vertex], q=True, ws=True,t=True)
    
    cmds.select(cl=True)
    
    CreateJoint= cmds.joint(n=(NewName+'_J_'+str(num)), r=1)

    ctl= cmds.circle(nr=(0, 0, 1), n=(CreateJoint+'_CTL'), r=1)[0]

    zgroup = cmds.group(n="Z_" + ctl)

    pgroup = cmds.group(n="P_" + ctl)

    cmds.select(cl=True)

    cmds.xform(pgroup,ws=True,t=position)

    cmds.xform(pgroup, ws=True, ro=orientation)

    cmds.parent(CreateJoint,ctl)

    cmds.select(cl=True)
    emparentarTrans = cmds.xform (CreateJoint, ws=True, t=vertex)
    num=num+1
    if lsel>1:
        cmds.progressBar(progressControl, edit=True, step=1)
cmds.pause( sec=.5 )
cmds.deleteUI( window, control=True )