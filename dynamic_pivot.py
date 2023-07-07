import Mutant_Tools
import Mutant_Tools.Utils.Rigging
from Mutant_Tools.Utils.Rigging import main_mutant
import imp

imp.reload(Mutant_Tools.Utils.Rigging.main_mutant)
mt = main_mutant.Mutant()


def dinamic_pivot(selection):
    ctrl = mt.curve(input='', type='cube', rename=True, custom_name=True, name='Dinamic_Pivot_{}'.format(selection),
                    size=1)
    cmds.select(cl=True)
    grp_ctrl = cmds.group(n='{}_Grp'.format(ctrl), em=True)
    get_position = cmds.xform(ctrl, ws=True, q=True, t=True)
    get_orient = cmds.xform(ctrl, ws=True, q=True, ro=True)
    cmds.xform(grp_ctrl, ws=True, t=get_position)
    cmds.xform(grp_ctrl, ws=True, ro=get_orient)
    cmds.parent(ctrl, grp_ctrl)

    cmds.connectAttr('{}.translate'.format(ctrl), '{}.rotatePivot'.format(selection))


dinamic_pivot(cmds.ls(sl=True)[0])