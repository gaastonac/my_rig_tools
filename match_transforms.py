import maya.cmds as cmds
'''This is a tool of match transforms of two objects'''

selection = cmds.ls (sl=True)

get_position = cmds.xform (selection[1], ws=True, q=True, t=True)

get_rot = cmds.xform (selection[1], ws=True, q=True, ro=True)

get_scale = cmds.xform(selection[1],ws=True,q=True,s=True)

cmds.xform (selection[0], ws=True, t=get_position)

cmds.xform (selection[0], ws=True, ro=get_rot)

cmds.xform (selection[0], ws=True, s=get_scale)

cmds.select(d=True)

#Hola Mundo#