import maya.cmds as cmds
sel = cmds.ls(sl=True)
list_connections = cmds.listConnections(sel[0],s=True,p=True,type='animCurveUL')
