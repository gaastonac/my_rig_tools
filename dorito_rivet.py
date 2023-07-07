def rivets_ctrls(geometry, selection_ctrls):
    grp_rivets = cmds.group(n='Rivets_Grp', em=True)

    for ctrl in selection_ctrls:
        # create rivet #

        uvpin_node = cmds.createNode('uvPin', n='Rivet_{}_node'.format(ctrl))

        locator = cmds.spaceLocator(n='Rivet_{}_Loc'.format(ctrl))[0]

        cmds.parent(locator, grp_rivets)

        cmds.connectAttr('{}.worldMesh'.format(geometry), '{}.deformedGeometry'.format(uvpin_node), f=True)

        cmds.connectAttr('{}.outputMatrix[0]'.format(uvpin_node), '{}.offsetParentMatrix'.format(locator), f=True)

        # get position ctrl#

        closest_node = cmds.createNode('closestPointOnMesh', n='CPOM_{}'.format(ctrl))

        cmds.connectAttr('{}.worldMesh'.format(geometry), '{}.inMesh'.format(closest_node), f=True)

        pos_ctrl = cmds.xform(ctrl, ws=True, q=True, t=True)

        rot_ctrl = cmds.xform(ctrl, ws=True, q=True, ro=True)

        scale_ctrl = cmds.xform(ctrl, ws=True, q=True, s=True)

        cmds.setAttr('{}.inPositionX'.format(closest_node), pos_ctrl[0])
        cmds.setAttr('{}.inPositionY'.format(closest_node), pos_ctrl[1])
        cmds.setAttr('{}.inPositionZ'.format(closest_node), pos_ctrl[2])

        parameter_u = cmds.getAttr('{}.parameterU'.format(closest_node))

        parameter_v = cmds.getAttr('{}.parameterV'.format(closest_node))

        # set parameters uv to coordinate uvpin#

        cmds.setAttr('{}.coordinate[0].coordinateU'.format(uvpin_node), parameter_u)

        cmds.setAttr('{}.coordinate[0].coordinateV'.format(uvpin_node), parameter_v)

        cmds.delete(closest_node)

        # create grps offset#

        offset_ctrl = cmds.listRelatives(ctrl, p=True)[0]

        inverse_grp = cmds.group(n='{}_Inverse_Grp'.format(ctrl), em=True)

        point_grp = cmds.group(n='{}_Point_Grp'.format(ctrl))

        cmds.xform(point_grp, ws=True, t=pos_ctrl)
        cmds.xform(point_grp, ws=True, ro=rot_ctrl)
        cmds.xform(point_grp, ws=True, s=scale_ctrl)

        cmds.parent(point_grp, offset_ctrl)

        cmds.parent(ctrl, inverse_grp)

        # offset

        offset_value = cmds.createNode('transposeMatrix', n='{}_offset_tm'.format(ctrl))

        offset_mm = cmds.createNode('multMatrix', n='{}_Offset_Mm'.format(ctrl))

        cmds.connectAttr('{}.worldMatrix'.format(point_grp), '{}.matrixIn[0]'.format(offset_mm))

        cmds.connectAttr('{}.worldInverseMatrix'.format(locator), '{}.matrixIn[1]'.format(offset_mm))

        cmds.connectAttr('{}.matrixSum'.format(offset_mm), '{}.inputMatrix'.format(offset_value))

        cmds.disconnectAttr('{}.matrixSum'.format(offset_mm), '{}.inputMatrix'.format(offset_value))

        cmds.delete(offset_mm)

        # point constraint rivet to point_grp#

        point_mm = cmds.createNode('multMatrix', n='{}_PointConstraint_Mm'.format(ctrl))

        point_dcm = cmds.createNode('decomposeMatrix', n='{}_PointConstraint_Dcm'.format(ctrl))

        cmds.connectAttr('{}.inputMatrix'.format(offset_value), '{}.matrixIn[0]'.format(point_mm), f=True)

        cmds.connectAttr('{}.worldMatrix[0]'.format(locator), '{}.matrixIn[1]'.format(point_mm), f=True)

        cmds.connectAttr('{}.worldInverseMatrix[0]'.format(offset_ctrl), '{}.matrixIn[2]'.format(point_mm), f=True)

        cmds.connectAttr('{}.matrixSum'.format(point_mm), '{}.inputMatrix'.format(point_dcm), f=True)

        cmds.connectAttr('{}.outputTranslate'.format(point_dcm), '{}.translate'.format(point_grp), f=True)

        # cmds.pointConstraint(locator,point_grp,mo=True)

        inverse_dcm = cmds.createNode('decomposeMatrix', n='{}_Inverse_Dcm'.format(ctrl))

        cmds.connectAttr('{}.inverseMatrix'.format(ctrl), '{}.inputMatrix'.format(inverse_dcm))

        cmds.connectAttr('{}.outputTranslate'.format(inverse_dcm), '{}.translate'.format(inverse_grp))

        cmds.connectAttr('{}.outputRotate'.format(inverse_dcm), '{}.rotate'.format(inverse_grp))


rivets_ctrls('C_Body_hi', cmds.ls(sl=True))
