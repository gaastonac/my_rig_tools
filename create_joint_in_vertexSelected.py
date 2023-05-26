import maya.cmds as cmds

sel = cmds.ls(selection=True, fl=True)
lsel = len(sel)
name = sel[0]
print name
NewName = name.split('.')[0]
print NewName

# Create a custom progressBar in a windows ...
window = cmds.window()
cmds.columnLayout()

if lsel > 1:
    progressControl = cmds.progressBar(maxValue=lsel - 1, width=300)

    cmds.showWindow(window)

for vertex in range(lsel):
    vertex = cmds.xform(sel[vertex], q=True, ws=True, t=True)
    print vertex
    cmds.select(d=True)
    CreateJoint = cmds.joint(n=(NewName + "_Joint"), r=1)
    emparentarTrans = cmds.xform(CreateJoint, ws=True, t=vertex)
    if lsel > 1:
        cmds.progressBar(progressControl, edit=True, step=1)
cmds.pause(sec=.5)
cmds.deleteUI(window, control=True)