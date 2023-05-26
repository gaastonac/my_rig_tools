# rivets on mesh#

for ctl in cmds.ls(sl=True):
    # create follicle #
    cmds.createNode('follicle')
    cmds.pickWalk(d='up')
    follicle = cmds.rename('{}_fl'.format(ctl))
    cmds.connectAttr('{}Shape.outRotate'.format(follicle), '{}.r'.format(follicle), f=True)
    cmds.connectAttr('{}Shape.outTranslate'.format(follicle), '{}.t'.format(follicle), f=True)

