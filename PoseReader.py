import maya.cmds as cmds

name_pose_reader = 'arm'

def create_node(node=None,name='None'):

    node = cmds.createNode(node,n=name)
    return node
def create_locs (prefix = ''):

    global base_locator

    global target_locator

    global reader_locator

    base_locator = cmds.spaceLocator(n='{}_Base'.format(prefix))[0]

    target_locator = cmds.spaceLocator(n='{}_Target'.format(prefix))[0]

    reader_locator = cmds.spaceLocator(n='{}_Reader'.format(prefix))[0]

def pose_reader(set_cone_angle = None):

    cmds.addAttr(target_locator,
                 ln='cone_angle',
                 at='double',
                 dv=set_cone_angle,
                 k=True)

    cmds.addAttr(target_locator,
                 ln='value_multiply',
                 at='double',
                 dv=1,
                 k=True)

    cmds.addAttr(target_locator,
                 ln='output_weight',
                 at='double',
                 dv=0,
                 k=True)

    av_vector_target_base = create_node('plusMinusAverage' ,  'AV_{}_Vector_Target_Base'.format(name_pose_reader))

    cmds.setAttr('{}.operation'.format(av_vector_target_base), 3)

    av_vector_reader_base = create_node('plusMinusAverage' , 'AV_{}_Vector_Reader_Base'.format(name_pose_reader))

    cmds.setAttr('{}.operation'.format(av_vector_reader_base), 3)

    '''Create Vector Target-Base'''

    cmds.connectAttr('{}Shape.worldPosition[0]'.format(target_locator) , '{}.input3D[0]'.format(av_vector_target_base))

    cmds.connectAttr('{}Shape.worldPosition[0]'.format(base_locator) , '{}.input3D[1]'.format(av_vector_target_base))

    '''Create Vector Reader-Base'''

    cmds.connectAttr('{}Shape.worldPosition[0]'.format(reader_locator) , '{}.input3D[0]'.format(av_vector_reader_base))

    cmds.connectAttr('{}Shape.worldPosition[0]'.format(base_locator) , '{}.input3D[1]'.format(av_vector_reader_base))

    angleBtwn_node = create_node('angleBetween','ABT_{}'.format(name_pose_reader))

    cmds.connectAttr('{}.output3D'.format(av_vector_target_base) , '{}.vector1'.format(angleBtwn_node))

    cmds.connectAttr('{}.output3D'.format(av_vector_reader_base) , '{}.vector2'.format(angleBtwn_node))

    mdl_multiply_node = create_node('multDoubleLinear', 'MDL_{}'.format(name_pose_reader))

    cmds.connectAttr('{}.cone_angle'.format(target_locator), '{}.input1'.format(mdl_multiply_node))

    cmds.connectAttr('{}.value_multiply'.format(target_locator),'{}.input2'.format(mdl_multiply_node))

    md_node = create_node('multiplyDivide', 'MD_{}'.format(name_pose_reader))

    cmds.setAttr('{}.operation'.format(md_node),2)
    
    cmds.connectAttr('{}.angle'.format(angleBtwn_node), '{}.input1X'.format(md_node))

    cmds.connectAttr('{}.output'.format(mdl_multiply_node), '{}.input2X'.format(md_node))

    rv_node = create_node('remapValue', 'RV_{}'.format(name_pose_reader))

    cmds.setAttr('{}.inputMin'.format(rv_node), 1)

    cmds.setAttr('{}.inputMax'.format(rv_node), 0)

    cmds.connectAttr('{}.outputX'.format(md_node), '{}.inputValue'.format(rv_node))

    cmds.connectAttr('{}.outValue')
create_locs(name_pose_reader)

pose_reader(90)



