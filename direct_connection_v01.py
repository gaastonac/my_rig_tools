import maya.cmds as cmds

# Make a new window

if cmds.window("Direct Connection",exists=True):

    cmds.deleteUI("Direct Connection")

window = cmds.window("Direct Connection",title="Direct Connection", iconName='Short Name',
                     s=False,widthHeight=(300, 200))

cmds.columnLayout( adjustableColumn=True )

cmds.separator( height=5, style='double' )

cmds.text ('Create by. Gaastonac')

cmds.separator( height=10, style='double' )

cmds.text ('Direct Connection')

cmds.separator( height=10, style='double' )

cmds.button( label='Connect', command=('Translate()'),h=40)

cmds.separator( height=10, style='double' )

cmds.rowColumnLayout(numberOfColumns=3, columnWidth=[ (1,90),(2,90),(3,90)], columnOffset=[(4,'right',3)])

TranslateXx=cmds.checkBox(label='Translate X')

TranslateYx=cmds.checkBox(label='Translate Y')

TranslateZx=cmds.checkBox(label='Translate Z')

RotateXx=cmds.checkBox(label='Rotate X',w=1,h=20)

RotateYx=cmds.checkBox(label='Rotate Y',w=1,h=20)

RotateZx=cmds.checkBox(label='Rotate Z',w=1,h=20)

ScaleXx=cmds.checkBox(label='Scale X',w=1,h=20)

ScaleYx=cmds.checkBox(label='Scale Y',w=1,h=20)

ScaleZx=cmds.checkBox(label='Scale Z',w=1,h=20)

Text_Vacio=cmds.text( label='' )

All=cmds.checkBox(label='ALL',w=1,h=40)

Text_Vacio=cmds.text( label='' )

cmds.showWindow( window )

def Translate():
    sel= cmds.ls (selection=True)

    lsel= len(sel)-1

    for J in range(lsel):

        checkboxAll= cmds.checkBox(All, q=True, v=True)

        checkboxTranslateXx= cmds.checkBox(TranslateXx, q=True, v=True)

        checkboxTranslateYx= cmds.checkBox(TranslateYx, q=True, v=True)

        checkboxTranslateZx= cmds.checkBox(TranslateZx, q=True, v=True)

        checkboxRotateXx= cmds.checkBox(RotateXx, q=True, v=True)

        checkboxRotateYx= cmds.checkBox(RotateYx, q=True, v=True)

        checkboxRotateZx= cmds.checkBox(RotateZx, q=True, v=True)

        checkboxScaleXx= cmds.checkBox(ScaleXx, q=True, v=True)

        checkboxScaleYx= cmds.checkBox(ScaleYx, q=True, v=True)

        checkboxScaleZx= cmds.checkBox(ScaleZx, q=True, v=True)

        if checkboxAll==True:

            Translate=cmds.connectAttr('{}.translate'.format(sel[J]),'{}.translate'.format(sel[J+1]), f=True)

            Rotate=cmds.connectAttr('{}.rotate'.format(sel[J]),'{}.rotate'.format(sel[J+1]), f=True)

            Scale=cmds.connectAttr('{}.scale'.format(sel[J]),'{}.scale'.format(sel[J+1]), f=True)

        if checkboxTranslateXx==True:

            TranslateX=cmds.connectAttr('{}.translateX'.format(sel[J]),'{}.translateX'.format(sel[J+1]), f=True)

        if checkboxTranslateYx==True:

            TranslateY=cmds.connectAttr('{}.translateY'.format(sel[J]),'{}.translateY'.format(sel[J+1]), f=True)

        if checkboxTranslateZx==True:

            TranslateZ=cmds.connectAttr('{}.translateZ'.format(sel[J]),'{}.translateZ'.format(sel[J+1]), f=True)

        if checkboxRotateXx==True:

            RotateX=cmds.connectAttr('{}.rotateX'.format(sel[J]),'{}.rotateX'.format(sel[J+1]), f=True)

        if checkboxRotateYx==True:

            RotateY=cmds.connectAttr('{}.rotateY'.format(sel[J]),'{}.rotateY'.format(sel[J+1]), f=True)

        if checkboxRotateZx==True:

            RotateZ=cmds.connectAttr('{}.rotateZ'.format(sel[J]),'{}.rotateZ'.format(sel[J+1]), f=True)

        if checkboxScaleXx==True:

            ScaleX=cmds.connectAttr('{}.scaleX'.format(sel[J]),'{}.scaleX'.format(sel[J+1]), f=True)

        if checkboxScaleYx==True:

            ScaleY=cmds.connectAttr('{}.scaleY'.format(sel[J]),'{}.scaleY'.format(sel[J+1]), f=True)

        if checkboxScaleZx==True:

            ScaleZ=cmds.connectAttr('{}.scaleZ'.format(sel[J]),'{}.scaleZ'.format(sel[J+1]), f=True)