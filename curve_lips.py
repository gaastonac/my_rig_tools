import maya.cmds as cmds


def create_poci(name,num):
    global node_poi
    node_poi = cmds.createNode('pointOnCurveInfo', name='poci_{}_{}'.format(name,num))

def create_locator(name,up_or_dwn,num):
    global locator
    locator = cmds.spaceLocator(n='{}_{}_{}_Loc'.format(name,up_or_dwn,num))[0]

def create_npo(name,num):
    global node_npo
    node_npo = cmds.createNode('nearestPointOnCurve', name='npo_{}_{}'.format(name,num))

selection = cmds.ls(sl=True)

cv_high = cmds.getAttr('{}.spans'.format(selection[1]))

for i in range (0,cv_high+1):

    create_poci(selection[0],i)

    cmds.connectAttr('{}.worldSpace'.format(selection[0]), '{}.inputCurve'.format(node_poi))

    create_locator('lip','lower',i)

    cmds.connectAttr('{}.position'.format(node_poi), '{}.translate'.format(locator))

    create_npo(selection[1],i)

    cmds.connectAttr('{}.worldSpace'.format(selection[0]), '{}.inputCurve'.format(node_npo))

    position_cv = cmds.pointPosition('{}.controlPoints[{}]'.format(selection[1],i))

    cmds.connectAttr('{}.parameter'.format(node_npo), '{}.parameter'.format(node_poi))

    cmds.setAttr('{}.inPositionX'.format(node_npo),position_cv[0])
    cmds.setAttr('{}.inPositionY'.format(node_npo),position_cv[1])
    cmds.setAttr('{}.inPositionZ'.format(node_npo),position_cv[2])
    
    cmds.disconnectAttr('{}.parameter'.format(node_npo), '{}.parameter'.format(node_poi))

    cmds.delete(node_npo)