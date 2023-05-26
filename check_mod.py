import maya.cmds as cmds

shapes = cmds.listRelatives('model_high_root',ad=True,type='mesh')


for shape in shapes:

    transform = shape.split('Shape')[0]
    try:
        connection = cmds.listConnections(shape, type='mesh', d=True,sh=True)[0]

    except:
        pass

    if connection == '{}_fbShape'.format(transform):

        cmds.warning("ALREADY EXISTS CONNECTION: connection: {} --> Shape: {}' ".format(connection,shape))
    else:

       cmds.warning("THIS SHAPE DONT HAVE CONNECTION : shape: {}".format(shape))
