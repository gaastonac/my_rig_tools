import maya.cmds as cmds

# Create a custom progressBar in a windows ...
window = cmds.window(title='Creating..')
cmds.columnLayout()


sel = cmds.ls(sl=True)[0]

his = cmds.listHistory(sel)

skin = cmds.ls(his, type='skinCluster')[0]

jnts = cmds.skinCluster(skin, q=True, inf=1)

if len(jnts) > 1:
    progressControl = cmds.progressBar(maxValue=len(jnts) - 1, width=300)

    cmds.showWindow(window)


vtxCnt = cmds.polyEvaluate(sel, v=1)

cmds.select(cl=True)

hola = cmds.skinCluster(skin, siv=jnts, e=True)

vtx = cmds.ls(sl=True, fl=True)

for jnt in jnts:
    pos = cmds.xform(jnt, q=True, ws=True, t=True)
    cl = cmds.cluster(n=jnt + 'CL')
    cmds.select(sel)
    cmds.setAttr(cl[1] + 'Shape.originX', pos[0])
    cmds.setAttr(cl[1] + 'Shape.originY', pos[1])
    cmds.setAttr(cl[1] + 'Shape.originZ', pos[2])

    cmds.setAttr(cl[1] + '.rotatePivot', pos[0], pos[1], pos[2])
    cmds.setAttr(cl[1] + '.scalePivot', pos[0], pos[1], pos[2])

    clSet = cmds.listConnections(cl[0], t='obectSet')
    print clSet

    for i in vtx:
        skinData = cmds.skinPercent(skin, i, q=True, t=jnt, v=True)
        cmds.percent(cl[0], i, v=skinData)
        print skinData
    if len(jnts) > 1:
        cmds.progressBar(progressControl, edit=True, step=1)
cmds.pause( sec=.5 )
cmds.deleteUI( window, control=True )