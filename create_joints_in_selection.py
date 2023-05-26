import maya.cmds as cmds
sel=cmds.ls(selection=True)
lsel= len(sel)
print sel, lsel

for seleccion in range(lsel):
    CreateJoint= cmds.joint(sel[seleccion],n=("M_Bind_" + sel[seleccion]),r=1)