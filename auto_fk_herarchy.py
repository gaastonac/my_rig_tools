import maya.cmds as cmds

jnts = cmds.ls(sl=True)
x = 0
for jnt in jnts:
    ctl = cmds.circle(n=jnt + '_CTL', nr=(1, 0, 0), r=2, ch=False)

    offset = cmds.group(n=jnt + '_Offset_Grp', w=True)

    position = cmds.xform(jnt, ws=True, q=True, t=True)

    orientation = cmds.xform(jnt, ws=True, q=True, ro=True)

    parent_position = cmds.xform(offset, ws=True, t=position)

    parent_rotation = cmds.xform(offset, ws=True, ro=orientation)

    cmds.parent(jnt, ctl)
    if len(jnts) > 1:
        if cmds.objExists(jnts[x - 1] + '_CTL'):
            cmds.parent(offset, jnts[x - 1])
            cmds.select(cl=True)
    x = x + 1
