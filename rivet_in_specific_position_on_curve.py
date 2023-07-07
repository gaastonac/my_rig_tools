def rvt_specific(crv):
    for loc in cmds.ls(sl=True):
        locator_Create = cmds.spaceLocator(n='Rvt_{}_00'.format(loc), a=True)[0]

        node_poc = cmds.shadingNode('pointOnCurveInfo', n='POS', au=True)
        node_npoc = cmds.shadingNode('nearestPointOnCurve', n='COS', au=True)

        cmds.connectAttr('{}.worldSpace'.format(crv), '{}.inputCurve'.format(node_poc), f=True)
        cmds.connectAttr('{}.worldSpace'.format(crv), '{}.inputCurve'.format(node_npoc), f=True)
        cmds.connectAttr('{}.worldPosition[0]'.format(loc), '{}.inPosition'.format(node_npoc), f=True)

        parameter = cmds.getAttr('{}.parameter'.format(node_npoc))

        setPU = cmds.setAttr('{}.parameter'.format(node_poc), parameter)

        cmds.delete(node_npoc)

        cmds.connectAttr('{}.position'.format(node_poc), '{}.translate'.format(locator_Create), f=True)


rvt_specific('L_shirt_crv')