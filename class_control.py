import maya.cmds as cmds


class Control:
    """"Create Control for Objs"""

    def __init__(self, prefix, name, radio):

        self.prefix = prefix

        self.name = name

        self.radio = radio

        ctl_obj = cmds.circle(n='{}_{}_CTL'.format(prefix, name), r=radio, nr=(0, 1, 0), ch=False)

        '''Color Ctl'''

        ctl_shape = cmds.listRelatives(ctl_obj, s=1)[0]

        cmds.setAttr('{}.ove'.format(ctl_shape), 1)

        if prefix.startswith('L'):

            cmds.setAttr('{}.ovc'.format(ctl_shape), 6)

        elif prefix.startswith('R'):

            cmds.setAttr('{}.ovc'.format(ctl_shape), 13)

        else:

            cmds.setAttr('{}.ovc'.format(ctl_shape), 17)


Control('L', 'Arm_Bind', 10)