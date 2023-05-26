import maya.cmds as cmds

if cmds.window("Create Nodes", exists=True):
    cmds.deleteUI("Create Nodes")
window = cmds.window("Create Nodes", title="Create Nodes", iconName='Short Name', s=False, widthHeight=(390, 310))
cmds.columnLayout(adjustableColumn=True)
cmds.separator(height=10, style='double')
cmds.text('Create by. Gaastonac')
cmds.separator(height=10, style='double')
Namereverse = cmds.textFieldGrp(l="Name", editable=True)
cmds.button(label='Create Reverse', command=('Reverse()'))
cmds.separator(height=10, style='double')
NameBlendcolors = cmds.textFieldGrp(l="Name", editable=True)
cmds.button(label='Create Blend Colors', command=('Colors()'))
cmds.separator(height=10, style='double')
NameMultiplyDivide = cmds.textFieldGrp(l="Name", editable=True)
cmds.button(label='Create MultiplyDivide', command=('MultiplyDivide()'))
cmds.separator(height=10, style='double')
NameplusMinusAverage = cmds.textFieldGrp(l="Name", editable=True)
cmds.button(label='Create plusMinusAverage', command=('Average()'))
cmds.separator(height=10, style='double')
NameCondition = cmds.textFieldGrp(l="Name", editable=True)
cmds.button(label='Create Condition', command=('Condition()'))
cmds.separator(height=10, style='double')
cmds.showWindow(window)


def Reverse():
    finalNameReverse = (cmds.textFieldGrp(Namereverse, q=True, text=True))
    if (finalNameReverse):
        NodeReverse = cmds.shadingNode('reverse', au=True, n=(finalNameReverse))
    else:
        NoodeReverse = cmds.shadingNode('reverse', au=True)


def MultiplyDivide():
    finalNameMultiplyDivide = (cmds.textFieldGrp(NameMultiplyDivide, q=True, text=True))
    if (finalNameMultiplyDivide):
        NodeMultiplyDivide = cmds.shadingNode('multiplyDivide', au=True, n=(finalNameMultiplyDivide))
    else:
        NoodeMultiplyDivide = cmds.shadingNode('multiplyDivide', au=True)


def Average():
    finalNameplusMinusAverage = (cmds.textFieldGrp(NameplusMinusAverage, q=True, text=True))
    if (finalNameplusMinusAverage):
        NodeplusMinusAverage = cmds.shadingNode('plusMinusAverage', au=True, n=(finalNameplusMinusAverage))
    else:
        NoodeplusMinusAverage = cmds.shadingNode('plusMinusAverage', au=True)


def Colors():
    finalColors = (cmds.textFieldGrp(NameBlendcolors, q=True, text=True))
    if (finalColors):
        NodeColors = cmds.shadingNode('blendColors', au=True, n=(finalColors))
    else:
        NodeColors = cmds.shadingNode('blendColors', au=True)


def Condition():
    finalNameCondition = (cmds.textFieldGrp(NameCondition, q=True, text=True))
    if (finalNameCondition):
        NodeCondition = cmds.shadingNode('condition', au=True, n=(finalNameCondition))
    else:
        NoodeCondition = cmds.shadingNode('condition', au=True)
