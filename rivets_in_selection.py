import maya.cmds as cmds


def Get_Rot(obj):
    global rot_sel
    rot_sel = cmds.xform(obj, q=True, ws=True, ro=True)


def Parent_Trans(obj):
    parent_trans = cmds.xform(obj, ws=True, t=pos)


def Parent_Rot(obj):
    parent_rot = cmds.xform(obj, ws=True, ro=rot_sel)


for i in cmds.ls(sl=True):
    prefix = str(i)
    pos = cmds.xform(i, q=True, ws=True, t=True)
    nrb = cmds.nurbsPlane(n=prefix + '_Nrb', p=(0, 0, 0), ax=(0, 1, 0), ch=False)[0]
    Get_Rot(i)
    Parent_Trans(nrb)
    Parent_Rot(nrb)
    offset = cmds.group(n='Z_' + nrb, em=True)
    Parent_Trans(offset)
    Parent_Rot(offset)
    cmds.parent(nrb,offset)

    XYZ = ('X', 'Y', 'Z')
    num_pos = 30
    num_normal = 0
    num_tU = 10
    num_tV = 20

    loc_rvt = cmds.spaceLocator(n='RVT_'+prefix + '_Loc', a=True)[0]
    cmds.select(cl=True)

    node_pos = cmds.shadingNode('pointOnSurfaceInfo', n='POS_RVT_' + prefix, au=True)
    node_fbfm = cmds.shadingNode('fourByFourMatrix', n='FBFM_RVT_' + prefix, au=True)
    node_dcm = cmds.shadingNode('decomposeMatrix', n='DCM_RVT_' + prefix, au=True)
    node_dcm_proj = cmds.shadingNode('decomposeMatrix', n='DCM_Proj_' + prefix, au=True)
    cmds.select(cl=True)

    for xyz in XYZ:
        cmds.connectAttr(node_pos + '.position' + xyz, node_fbfm + '.in' + str(num_pos), f=True)
        cmds.connectAttr(node_pos + '.normal' + xyz, node_fbfm + '.in0' + str(num_normal), f=True)
        cmds.connectAttr(node_pos + '.tangentU' + xyz.lower(), node_fbfm + '.in' + str(num_tU), f=True)
        cmds.connectAttr(node_pos + '.tangentV' + xyz.lower(), node_fbfm + '.in' + str(num_tV), f=True)
        num_pos = num_pos + 1
        num_normal = num_normal + 1
        num_tU = num_tU + 1
        num_tV = num_tV + 1

    cmds.connectAttr(node_fbfm + '.output', node_dcm + '.inputMatrix', f=True)
    cmds.connectAttr(nrb + '.worldSpace', node_pos + '.inputSurface', f=True)
    cmds.connectAttr(node_dcm + '.outputRotate', loc_rvt + '.rotate', f=True)
    cmds.connectAttr(node_dcm + '.outputTranslate', loc_rvt + '.translate', f=True)
    cmds.connectAttr(loc_rvt + '.worldMatrix', node_dcm_proj + '.inputMatrix', f=True)
    cmds.setAttr(node_pos + '.parameterU', .5)
    cmds.setAttr(node_pos + '.parameterV', .5)