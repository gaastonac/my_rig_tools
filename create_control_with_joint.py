import maya.cmds as cmds

sel = cmds.ls(selection=True)

for obj_selected in sel:
    joint = cmds.joint(obj_selected, n=(obj_selected + '_CTL_J'), r=1)

    ctl = cmds.circle(nr=(0, 1, 0), n=(obj_selected + '_CTL'), r=1)[0]

    zgroup = cmds.group(n="Z_" + ctl)

    pgroup = cmds.group(n="P_" + ctl)

    cmds.select(cl=True)

    position = cmds.xform(joint, ws=True, q=True, t=True)

    orientation = cmds.xform(joint, ws=True, q=True, ro=True)

    cmds.xform(pgroup, ws=True, t=position)

    cmds.xform(pgroup, ws=True, ro=orientation)

    cmds.parent(pgroup, obj_selected)

    cmds.parent(joint, ctl)

    cmds.parent(pgroup, w=True)

    cmds.select(cl=True)
