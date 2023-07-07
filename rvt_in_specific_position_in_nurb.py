def Create_Rivets_Spans(nrb):
    for loc in cmds.ls(sl=True):
        locator_Create = cmds.spaceLocator(n='Rvt_{}_00'.format(loc), a=True)[0]

        node_pos = cmds.shadingNode('pointOnSurfaceInfo', n='POS', au=True)
        node_closest = cmds.shadingNode('closestPointOnSurface', n='COS', au=True)

        cmds.connectAttr('{}.worldSpace'.format(nrb), '{}.inputSurface'.format(node_closest), f=True)
        cmds.connectAttr('{}.worldPosition[0]'.format(loc), '{}.inPosition'.format(node_closest), f=True)

        u_value = cmds.getAttr('{}.parameterU'.format(node_closest))
        v_value = cmds.getAttr('{}.parameterV'.format(node_closest))

        setPU = cmds.setAttr('{}.parameterU'.format(node_pos), u_value)
        setPV = cmds.setAttr('{}.parameterV'.format(node_pos), v_value)

        cmds.delete(node_closest)

        node_fbfm = cmds.shadingNode('fourByFourMatrix', n='FBFM', au=True)
        node_dcm = cmds.shadingNode('decomposeMatrix', n='DCM', au=True)

        cmds.connectAttr('{}.positionX'.format(node_pos), '{}.in30'.format(node_fbfm), f=True)
        cmds.connectAttr('{}.positionY'.format(node_pos), '{}.in31'.format(node_fbfm), f=True)
        cmds.connectAttr('{}.positionZ'.format(node_pos), '{}.in32'.format(node_fbfm), f=True)

        cmds.connectAttr('{}.normalX'.format(node_pos), '{}.in00'.format(node_fbfm), f=True)
        cmds.connectAttr('{}.normalY'.format(node_pos), '{}.in01'.format(node_fbfm), f=True)
        cmds.connectAttr('{}.normalZ'.format(node_pos), '{}.in02'.format(node_fbfm), f=True)

        cmds.connectAttr('{}.tangentUx'.format(node_pos), '{}.in10'.format(node_fbfm), f=True)
        cmds.connectAttr('{}.tangentUy'.format(node_pos), '{}.in11'.format(node_fbfm), f=True)
        cmds.connectAttr('{}.tangentUz'.format(node_pos), '{}.in12'.format(node_fbfm), f=True)

        cmds.connectAttr('{}.tangentVx'.format(node_pos), '{}.in20'.format(node_fbfm), f=True)
        cmds.connectAttr('{}.tangentVy'.format(node_pos), '{}.in21'.format(node_fbfm), f=True)
        cmds.connectAttr('{}.tangentVz'.format(node_pos), '{}.in22'.format(node_fbfm), f=True)

        cmds.connectAttr('{}.output'.format(node_fbfm), '{}.inputMatrix'.format(node_dcm), f=True)
        cmds.connectAttr('{}.worldSpace'.format(nrb), '{}.inputSurface'.format(node_pos), f=True)

        cmds.connectAttr('{}.outputRotate'.format(node_dcm), '{}.rotate'.format(locator_Create), f=True)
        cmds.connectAttr('{}.outputTranslate'.format(node_dcm), '{}.translate'.format(locator_Create), f=True)


Create_Rivets_Spans('follow_tweak_sweater_ctls_nrb')