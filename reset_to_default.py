''' script for reset control to bind pose '''

import maya.cmds as cmds

sel = cmds.ls(selection=True)

XYZ=('X','Y','Z')

for ctrl in sel:

    for xyz in XYZ:

        if cmds.getAttr ('{}.translate{}'.format(ctrl,xyz) ,lock=True)==False:

            cmds.setAttr ('{}.translate{}'.format(ctrl,xyz) ,0)

        if cmds.getAttr ('{}.rotate{}'.format(ctrl,xyz) ,lock=True)==False:

            cmds.setAttr ('{}.rotate{}'.format(ctrl,xyz) ,0)

        if cmds.getAttr ('{}.scale{}'.format(ctrl,xyz) ,lock=True)==False:

            cmds.setAttr ('{}.scale{}'.format(ctrl,xyz) ,1)