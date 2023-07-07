prefix = 'R'
up_dw = 'Dw'
locs = ['base', 'reader', 'target']
jnts = ['{}_Eyelids_Scale_Jnt'.format(prefix), '{}_Eyelids_{}_6_Jnt'.format(prefix, up_dw),
        '{}_Eyelids_Scale_Jnt'.format(prefix)]

for num, loc in enumerate(locs):
    locator = cmds.spaceLocator(n='{}_angle_{}_loc_{}'.format(prefix, loc, up_dw))[0]
    t = cmds.xform(jnts[num], ws=True, q=True, t=True)
    cmds.xform(locator, ws=True, t=t)
    cmds.parentConstraint(jnts[num], locator, mo=True)

locs = ['reader', 'target']
for loc in locs:
    vector_base_read = cmds.createNode('plusMinusAverage', n='{}_vector_Base_{}_{}'.format(prefix, loc, up_dw))
    cmds.setAttr('{}.operation'.format(vector_base_read), 2)
    cmds.connectAttr('{}_angle_{}_loc_{}.worldPosition'.format(prefix, loc, up_dw),
                     '{}.input3D[0]'.format(vector_base_read), f=True)
    cmds.connectAttr('{}_angle_base_loc_{}.worldPosition'.format(prefix, up_dw),
                     '{}.input3D[1]'.format(vector_base_read), f=True)

angle_between = cmds.createNode('angleBetween', n='{}_angleBetween_{}'.format(prefix, up_dw))
cmds.connectAttr('{}_vector_Base_target_{}.output3D'.format(prefix, up_dw),
                 '{}_angleBetween_{}.vector1'.format(prefix, up_dw), f=True)
cmds.connectAttr('{}_vector_Base_reader_{}.output3D'.format(prefix, up_dw),
                 '{}_angleBetween_{}.vector2'.format(prefix, up_dw), f=True)

rv_node = cmds.createNode('remapValue', n='{}_angle_remapValue_{}'.format(prefix, up_dw))
cmds.connectAttr('{}.angle'.format(angle_between), '{}.inputValue'.format(rv_node), f=True)