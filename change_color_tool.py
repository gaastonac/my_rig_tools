import maya.cmds as cmds

'''Tool for change override color to objects'''

if cmds.window("Color", exists=True):
    cmds.deleteUI("Color")

cmds.window('Color', title='Change Color', s=False, widthHeight=(400, 30))

cmds.columnLayout()


def slider(*args):

    for cv in cmds.ls(sl=True):

        color = cmds.colorSliderGrp(slider, query=True, rgb=True)

        cmds.setAttr('{}.overrideEnabled'.format(cv), 1)

        cmds.setAttr('{}.overrideRGBColors'.format(cv), 1)

        cmds.setAttr('{}.overrideColorRGB'.format(cv), color[0], color[1], color[2])


slider = cmds.colorSliderGrp(label='Color', rgb=(0, 0, 1), cc=slider)

cmds.showWindow()
