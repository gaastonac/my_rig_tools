#########CREATED BY.GAASTONAC#########
###Create_Grps_Offset###
import maya.cmds as cmds

for offset in cmds.ls(selection=True):  # for create offst

    obj_father = cmds.listRelatives(offset, p=True)  # query obj father of selection

    name = ("Z_" + str(offset))  # name input of offset

    num = 0  # num initial

    while cmds.objExists(name):  # if checked if name already exists in scene

        num = num + 1  # if name is already exists sum 1 to num

        name = ("Z_" + offset + "_" + str(num))  # added 1 number to name

    grp_offset = cmds.group(n=name, em=True)  # create grp offset

    position = cmds.xform(offset, ws=True, q=True, t=True)

    orientation = cmds.xform(offset, ws=True, q=True, ro=True)

    parent_position = cmds.xform(name, ws=True, t=position)

    parent_orientation = cmds.xform(name, ws=True, ro=orientation)

    if obj_father:
        cmds.parent(name, obj_father)

    cmds.parent(offset, name)
