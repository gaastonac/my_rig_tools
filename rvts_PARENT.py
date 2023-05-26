for i in cmds.ls(sl=True):
    print i
    DCM=cmds.listConnections(i,s=True,p=False)[0]
    print DCM
    FBFM=cmds.listConnections(DCM,s=True,type='fourByFourMatrix')[0]
    print FBFM
    MM=cmds.shadingNode('multMatrix',n='MM_'+i,au=True)
    cmds.select(cl=True)
    cmds.connectAttr(FBFM+'.output',MM+'.matrixIn[0]')
    cmds.connectAttr(i+'.parentInverseMatrix',MM+'.matrixIn[1]')
    cmds.connectAttr(MM+'.matrixSum',DCM+'.inputMatrix',f=True)
    
    
    