import maya.cmds as cmds
import maya.mel as mel

'''This tool cleane your scene, of unknow nodes, turtle node and unused nodes'''

if cmds.window("Clean_Nodes", exists=True):

    cmds.deleteUI("Clean_Nodes")

window = cmds.window("Clean_Nodes", title="Clean_Nodes", iconName='Short Name', s=False, widthHeight=(300, 130))

cmds.columnLayout(adjustableColumn=True)

cmds.separator(height=5, style='double')

cmds.text('Create by. Gaastonac')

cmds.separator(height=10, style='double')

cmds.button(label='Clean Nodes Unknown', command=('Nodes_Unknown()'))

cmds.separator(height=10, style='double')

cmds.button(label='Clean Nodes UnusedNode', command=('Nodes_UnusedNode()'))

cmds.separator(height=10, style='double')

cmds.button(label='Clean TurtleLayer', command=('Clean_Turtle()'))

cmds.separator(height=10, style='double')

cmds.showWindow(window)


def Nodes_Unknown():

    '''feel free to modify/delete lines commented as 1,2, or 3 depending on if you want to see,
    select, or delete the unknown nodes.'''

    selection= cmds.ls(typ="unknown")  # "Get" the nodes in scene labeled as unknown.

    cmds.select(selection)  # 2: select the unknown nodes

    cmds.delete(selection)  # 3: delete the unknown nodes


def Nodes_UnusedNode():

    mel.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "deleteUnusedNodes");')


def Clean_Turtle():

    cmds.lockNode('TurtleDefaultBakeLayer', l=0)

    cmds.delete('TurtleDefaultBakeLayer')