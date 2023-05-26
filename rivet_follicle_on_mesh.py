# rivets on mesh#

selection = cmds.ls(sl=True)
mesh = selection[-1]
selection.remove(selection[-1])
ctls = selection
for ctl in ctls:
    print mesh
    # create follicle #
    cmds.createNode('follicle')
    cmds.pickWalk(d='up')
    follicle = cmds.rename('{}_fl'.format(ctl))
    cmds.connectAttr('{}Shape.outRotate'.format(follicle), '{}.r'.format(follicle), f=True)
    cmds.connectAttr('{}Shape.outTranslate'.format(follicle), '{}.t'.format(follicle), f=True)


    cmds.connectAttr('{}Shape.outMesh'.format(mesh),'{}.inputMesh'.format(follicle),f=True)
    cmds.connectAttr('{}Shape.worldMatrix'.format(mesh), '{}.inputWorldMatrix'.format(follicle), f=True)

    closest_node = cmds.createNode('closestPointOnMesh',n='{}_cpom'.format(ctl))
    cmds.connectAttr('{}Shape.outMesh'.format(mesh), '{}.inMesh'.format(closest_node), f=True)
    decompose_node = cmds.createNode('decomposeMatrix',n='{}_dcm'.format(ctl))
    cmds.connectAttr('{}.worldMatrix'.format(ctl),'{}.inputMatrix'.format(decompose_node))
    cmds.connectAttr('{}.outputTranslate'.format(decompose_node),'{}.inPosition'.format(closest_node))

    cmds.connectAttr('{}.parameterU'.format(closest_node),'{}.parameterU'.format(follicle))
    cmds.connectAttr('{}.parameterV'.format(closest_node), '{}.parameterV'.format(follicle))

    cmds.disconnectAttr('{}.parameterU'.format(closest_node), '{}.parameterU'.format(follicle))
    cmds.disconnectAttr('{}.parameterV'.format(closest_node), '{}.parameterV'.format(follicle))

    cmds.delete(closest_node)

    cmds.select(cl=True)

    grp_inverse = cmds.group(n='{}_inverse_rivet'.format(ctl),em=True)
    grp_point = cmds.group(n='{}_point_rivet'.format(ctl))

    translate_info = cmds.xform(ctl,ws=True,q=True,t=True)
    rotate_info = cmds.xform(ctl, ws=True, q=True, ro=True)
    scale_info = cmds.xform(ctl, ws=True, q=True, s=True)

    cmds.xform(grp_point , ws=True,t=translate_info)
    cmds.xform(grp_point, ws=True, ro=rotate_info)
    cmds.xform(grp_point, ws=True, s=scale_info)

    parent_ctl = cmds.listRelatives(ctl,p=True)

    cmds.parent(grp_point,parent_ctl)
    cmds.parent(ctl,grp_inverse)

    cmds.pointConstraint(follicle,grp_point,mo=True)

    decompose_inverse_node = cmds.createNode('decomposeMatrix',n='{}_inverse'.format(ctl))
    cmds.connectAttr('{}.inverseMatrix'.format(ctl),'{}.inputMatrix'.format(decompose_inverse_node))
    cmds.connectAttr('{}.outputTranslate'.format(decompose_inverse_node),'{}.t'.format(grp_inverse))

