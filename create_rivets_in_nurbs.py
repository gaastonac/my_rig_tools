import maya.cmds as cmds
import maya.cmds as cmds

# Make a new window
if cmds.window("Rivets", exists=True):
    cmds.deleteUI("Rivets")

window = cmds.window("Rivets", title="Rivets", iconName='Short Name', s=False, widthHeight=(250, 145))
cmds.columnLayout(adjustableColumn=True)
cmds.separator(height=5, style='double')
cmds.text('Create by. Gaastonac')
cmds.separator(height=10, style='double')
cmds.button(label='Create Rivets Edge Nurb', command=('Create_Rivets_Edges()'), h=30)
cmds.separator(height=10, style='double')
cmds.button(label='Create Rivets Spans Nurb', command=('Create_Rivets_Spans()'), h=30)
cmds.separator(height=10, style='double')
cmds.button(label='Create Rivets Spans Curve', command=('Create_Rivets_Spans_Curve()'), h=30)
cmds.showWindow(window)


def Create_Rivets_Edges():
    sel = cmds.ls(selection=True)
    Gett_Edges_Nurb = cmds.getAttr(sel[0] + '.spansU')
    Repeticiones = 0

    if Gett_Edges_Nurb > 1:
        U = 'U'
        V = 'V'
        maxValue = cmds.getAttr(sel[0] + '.minMaxRangeU.maxValue' + U)
    else:
        U = 'V'
        V = 'U'
        maxValue = cmds.getAttr(sel[0] + '.minMaxRangeV.maxValue' + U)
        Gett_Edges_Nurb = cmds.getAttr(sel[0] + '.spansV')

    Distancia = 1 / float(Gett_Edges_Nurb) * maxValue

    for Loc in range(Gett_Edges_Nurb + 1):
        Locator_Create = cmds.spaceLocator(n='Loc_Rivet_' + (sel[0]) + '_00', a=True)[0]
        Node_POS = cmds.shadingNode('pointOnSurfaceInfo', n='POS', au=True)
        SetPU = cmds.setAttr((Node_POS) + '.parameter' + (U), Repeticiones * Distancia)
        SetPV = cmds.setAttr((Node_POS) + '.parameter' + (V), .5)
        Node_FBFM = cmds.shadingNode('fourByFourMatrix', n='FBFM', au=True)
        Node_DCM = cmds.shadingNode('decomposeMatrix', n='DCM', au=True)
        ConectPosX = cmds.connectAttr((Node_POS) + '.positionX', (Node_FBFM) + '.in30', f=True)
        ConectPosY = cmds.connectAttr((Node_POS) + '.positionY', (Node_FBFM) + '.in31', f=True)
        ConectPosZ = cmds.connectAttr((Node_POS) + '.positionZ', (Node_FBFM) + '.in32', f=True)
        ConectNX = cmds.connectAttr((Node_POS) + '.normalX', (Node_FBFM) + '.in00', f=True)
        ConectNY = cmds.connectAttr((Node_POS) + '.normalY', (Node_FBFM) + '.in01', f=True)
        ConectNZ = cmds.connectAttr((Node_POS) + '.normalZ', (Node_FBFM) + '.in02', f=True)
        ConectTUX = cmds.connectAttr((Node_POS) + '.tangentUx', (Node_FBFM) + '.in10', f=True)
        ConectTUY = cmds.connectAttr((Node_POS) + '.tangentUy', (Node_FBFM) + '.in11', f=True)
        ConectTUY = cmds.connectAttr((Node_POS) + '.tangentUz', (Node_FBFM) + '.in12', f=True)
        ConectTVX = cmds.connectAttr((Node_POS) + '.tangentVx', (Node_FBFM) + '.in20', f=True)
        ConectTVY = cmds.connectAttr((Node_POS) + '.tangentVy', (Node_FBFM) + '.in21', f=True)
        ConectTVY = cmds.connectAttr((Node_POS) + '.tangentVz', (Node_FBFM) + '.in22', f=True)
        ConectInputMatrix = cmds.connectAttr((Node_FBFM) + '.output', (Node_DCM) + '.inputMatrix', f=True)
        Surface_WS = cmds.connectAttr((sel[0]) + '.worldSpace', (Node_POS) + '.inputSurface', f=True)
        OutR = cmds.connectAttr((Node_DCM) + '.outputRotate', (Locator_Create) + '.rotate', f=True)
        OutP = cmds.connectAttr((Node_DCM) + '.outputTranslate', (Locator_Create) + '.translate', f=True)
        Repeticiones = Repeticiones + 1
        print Repeticiones


def Create_Rivets_Spans():
    sel = cmds.ls(selection=True)
    Gett_Spans_Nurb = cmds.getAttr(sel[0] + '.spansU')
    if Gett_Spans_Nurb > 1:
        U = 'U'
        V = 'V'
        maxValue = cmds.getAttr(sel[0] + '.minMaxRangeU.maxValue' + U)
    else:
        U = 'V'
        V = 'U'
        maxValue = cmds.getAttr(sel[0] + '.minMaxRangeV.maxValue' + U)
        Gett_Spans_Nurb = cmds.getAttr(sel[0] + '.spansV')

    Distancia = 1 / float(Gett_Spans_Nurb) * maxValue
    Repeticiones = Distancia / 2
    for Loc in range(Gett_Spans_Nurb):
        Locator_Create = cmds.spaceLocator(n='Loc_Rivet_' + (sel[0]) + '_00', a=True)[0]
        Node_POS = cmds.shadingNode('pointOnSurfaceInfo', n='POS', au=True)
        SetPU = cmds.setAttr((Node_POS) + '.parameter' + (U), Repeticiones)
        SetPV = cmds.setAttr((Node_POS) + '.parameter' + (V), .5)
        Node_FBFM = cmds.shadingNode('fourByFourMatrix', n='FBFM', au=True)
        Node_DCM = cmds.shadingNode('decomposeMatrix', n='DCM', au=True)
        ConectPosX = cmds.connectAttr((Node_POS) + '.positionX', (Node_FBFM) + '.in30', f=True)
        ConectPosY = cmds.connectAttr((Node_POS) + '.positionY', (Node_FBFM) + '.in31', f=True)
        ConectPosZ = cmds.connectAttr((Node_POS) + '.positionZ', (Node_FBFM) + '.in32', f=True)
        ConectNX = cmds.connectAttr((Node_POS) + '.normalX', (Node_FBFM) + '.in00', f=True)
        ConectNY = cmds.connectAttr((Node_POS) + '.normalY', (Node_FBFM) + '.in01', f=True)
        ConectNZ = cmds.connectAttr((Node_POS) + '.normalZ', (Node_FBFM) + '.in02', f=True)
        ConectTUX = cmds.connectAttr((Node_POS) + '.tangentUx', (Node_FBFM) + '.in10', f=True)
        ConectTUY = cmds.connectAttr((Node_POS) + '.tangentUy', (Node_FBFM) + '.in11', f=True)
        ConectTUY = cmds.connectAttr((Node_POS) + '.tangentUz', (Node_FBFM) + '.in12', f=True)
        ConectTVX = cmds.connectAttr((Node_POS) + '.tangentVx', (Node_FBFM) + '.in20', f=True)
        ConectTVY = cmds.connectAttr((Node_POS) + '.tangentVy', (Node_FBFM) + '.in21', f=True)
        ConectTVY = cmds.connectAttr((Node_POS) + '.tangentVz', (Node_FBFM) + '.in22', f=True)
        ConectInputMatrix = cmds.connectAttr((Node_FBFM) + '.output', (Node_DCM) + '.inputMatrix', f=True)
        Surface_WS = cmds.connectAttr((sel[0]) + '.worldSpace', (Node_POS) + '.inputSurface', f=True)
        OutR = cmds.connectAttr((Node_DCM) + '.outputRotate', (Locator_Create) + '.rotate', f=True)
        OutP = cmds.connectAttr((Node_DCM) + '.outputTranslate', (Locator_Create) + '.translate', f=True)
        Repeticiones = Repeticiones + Distancia
        print Repeticiones


def Create_Rivets_Spans_Curve():
    sel = cmds.ls(selection=True)
    Gett_Spans_Curve = cmds.getAttr(sel[0] + '.spans')
    print Gett_Spans_Curve
    Repeticiones = 0
    for Loc in range(Gett_Spans_Curve + 1):
        Locator_Create = cmds.spaceLocator(n='Loc_Rivet_' + (sel[0]) + '_00', a=True)[0]
        Node_POCI = cmds.shadingNode('pointOnCurveInfo', n='POCI', au=True)
        SetParameter = cmds.setAttr((Node_POCI) + '.parameter', Repeticiones)
        Surface_WS = cmds.connectAttr((sel[0]) + '.worldSpace', (Node_POCI) + '.inputCurve', f=True)
        OutP = cmds.connectAttr((Node_POCI) + '.position', (Locator_Create) + '.translate', f=True)
        Repeticiones = Repeticiones + 1
        print Repeticiones