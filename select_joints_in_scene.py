import maya.cmds as cmds
selected = cmds.ls (type='joint')
cmds.select(selected)