import maya.cmds as cmds
# Make a new window
if cmds.window("MatrixConstraint",exists=True):
    cmds.deleteUI("MatrixConstraint")
window = cmds.window("MatrixConstraint",title="MatrixConstraint", iconName='Short Name',s=True, widthHeight=(300, 170) )
cmds.columnLayout( adjustableColumn=True )
cmds.separator( height=10, style='double' )
cmds.text ('Create by. Gaastonac')
cmds.text('Tool MatrixConstraint')
cmds.separator( height=10, style='double' )
cmds.button( label='Apply', command=('apply()'),h=40)
cmds.separator( height=20, style='double' )
cmds.rowColumnLayout(numberOfColumns=3, columnWidth=[ (1,90),(3,90),(3,90)], columnOffset=[(4,'right',3)])
cmds.text('CheckBox')
Offset=cmds.checkBox(label='MantainOffset' )
cmds.setParent( '..' )
cmds.separator( height=10, style='double' )
cmds.rowColumnLayout(numberOfColumns=4, columnWidth=[ (1,90),(2,90),(3,90)], columnOffset=[(4,'right',3)])
cmds.text('CheckBox')
ParentM=cmds.checkBox(label='Parent' )
OrientM=cmds.checkBox(label='Orient' )
ScaleM=cmds.checkBox(label='Scale' )
cmds.showWindow( window )

def DCM(Name):#Funcion para crear nodo de decompose matrix

    global Node_DCM

    Node_DCM=cmds.shadingNode('decomposeMatrix',n=Name,au=True)

def MM(Name):#Funcion para crear nodo de mult matrix

    global Node_MM

    Node_MM=cmds.shadingNode('multMatrix',n=Name,au=True)

def connect(obj1,obj2):

    cmds.connectAttr(obj1,obj2,f=True)

def attrOffset(target):

    cmds.addAttr(target,ln='offset',at='matrix')
    
def apply():

    list_objs=cmds.ls(sl=True)

    checkboxParent= cmds.checkBox(ParentM, q=True, v=True)

    checkboxOffset= cmds.checkBox(Offset, q=True, v=True)

    if checkboxParent==True:

        if checkboxOffset==True:
            # Create MultiMatrix
            MM('MM_'+'OffsetParentMatrix_{}'.format(list_objs[1]))

            # Connect WorldMatrixTargetToMultiMatrix
            connect('{}.worldMatrix[0]'.format(list_objs[1]),'{}.matrixIn[0]'.format(Node_MM))

            # Connect InverseWorldMatrixTargetToMultiMatrix
            connect('{}.worldInverseMatrix[0]'.format(list_objs[0]),'{}.matrixIn[1]'.format(Node_MM))
            
            queryOffset=cmds.attributeQuery('offset',n=list_objs[1],ex=True)

            if queryOffset==False:

                attrOffset(list_objs[1])
            
            connect('{}.matrixSum'.format(Node_MM),'{}.offset'.format(list_objs[1]))
            
            cmds.disconnectAttr('{}.matrixSum'.format(Node_MM),'{}.offset'.format(list_objs[1]))

            cmds.delete(Node_MM)
            
            DCM('DCM_ParentMatrix_{}'.format(list_objs[1]))#Create DecomposeMatrix

            MM('MM_ParentMatrix_{}'.format(list_objs[1]))#Create MultiMatrix
            
            connect('{}.offset'.format(list_objs[1]),'{}.matrixIn[0]'.format(Node_MM))
            
            connect('{}.worldMatrix[0]'.format(list_objs[0]),'{}.matrixIn[1]'.format(Node_MM))#Connect WorldMatrixToMultiMatrix
            
            connect('{}.parentInverseMatrix'.format(list_objs[1]),'{}.matrixIn[2]'.format(Node_MM))#Connect ParentInverseMatrixToMultiMatrix
            
            connect('{}.matrixSum'.format(Node_MM),'{}.inputMatrix'.format(Node_DCM))#Connect MatrixSum To InputMatrix Decompose
            
            connect('{}.outputTranslate'.format(Node_DCM),'{}.translate'.format(list_objs[1]))#Connect Output Translate to Target

            connect('{}.outputRotate'.format(Node_DCM),'{}.rotate'.format(list_objs[1]))#Connect Output Translate to Target
          

        else:
            
            DCM('DCM_ParentMatrix_{}'.format(list_objs[1]))#Create DecomposeMatrix

            MM('MM_ParentMatrix_{}'.format(list_objs[1]))#Create MultiMatrix
            
            connect('{}.worldMatrix[0]'.format(list_objs[0]),'{}.matrixIn[0]'.format(Node_MM))#Connect WorldMatrixToMultiMatrix
            
            connect('{}.parentInverseMatrix'.format(list_objs[1]),'{}.matrixIn[1]'.format(Node_MM))#Connect ParentInverseMatrixToMultiMatrix
            
            connect('{}.matrixSum'.format(Node_MM),'{}.inputMatrix'.format(Node_DCM))#Connect MatrixSum To InputMatrix Decompose
            
            connect('{}.outputTranslate'.format(Node_DCM),'{}.translate'.format(list_objs[1]))#Connect Output Translate to Target

            connect('{}.outputRotate'.format(Node_DCM),'{}.rotate'.format(list_objs[1]))#Connect Output Translate to Target