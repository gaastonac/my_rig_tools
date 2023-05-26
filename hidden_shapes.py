from maya import cmds
sel= cmds.ls (selection=True)
lsel= len(sel)
print sel, lsel
for node in range(lsel):
    cmds.setAttr(sel[node] + ".ihi", 0)