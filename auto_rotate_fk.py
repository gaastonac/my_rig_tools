import Mutant_Tools
import Mutant_Tools.Utils.Rigging
from Mutant_Tools.Utils.Rigging import main_mutant
import imp

imp.reload(Mutant_Tools.Utils.Rigging.main_mutant)
mt = main_mutant.Mutant()


def ctrl_rotator(name_ctrl):
    global ctrl_crv
    ctrl_crv = mt.curve(input='', type='sphere', rename=True, custom_name=True, name='Rotator_{}'.format(name_ctrl),
                        size=1)


def get_position(obj):
    global position
    position = cmds.xform(obj, ws=True, q=True, t=True)


def get_orient(obj):
    global orient
    orient = cmds.xform(obj, ws=True, q=True, ro=True)


selection = cmds.ls(sl=True)
parent_ini_ctrl = cmds.listRelatives(selection[0], p=True)[0]

ini_ctrl = cmds.select(selection[0])
ctrl_autorotate = ctrl_rotator(selection[0])
cmds.parent(ctrl_crv, parent_ini_ctrl)
cmds.select(cl=True)

for ctrl in selection:
    grp_sdk = cmds.group(n='{}_Grp_SDK'.format(ctrl), em=True)
    grp_offset_sdk = cmds.group(n='{}_Offset_Grp_SDK'.format(ctrl))

    cmds.select(cl=True)

    parent_ctrl = cmds.listRelatives(ctrl, p=True)[0]

    get_position(ctrl)
    get_orient(ctrl)

    cmds.xform(grp_offset_sdk, ws=True, t=position)
    cmds.xform(grp_offset_sdk, ws=True, ro=orient)

    cmds.parent(grp_offset_sdk, parent_ctrl)
    cmds.parent(ctrl, grp_sdk)

    cmds.select(cl=True)

    cmds.connectAttr('{}.r'.format(ctrl_crv), '{}.r'.format(grp_sdk), f=True)