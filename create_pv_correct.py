import maya.api.OpenMaya as om

arm_pos = om.MVector(cmds.xform('joint1',q=True,rp=True,ws=True))
elbow_pos = om.MVector(cmds.xform('joint2',q=True,rp=True,ws=True))
wrist_pos = om.MVector(cmds.xform('joint3',q=True,rp=True,ws=True))

arm_to_wrist = wrist_pos - arm_pos

arm_to_wrist_scaled = arm_to_wrist / 2

mid_point = arm_pos + arm_to_wrist_scaled

mid_point_to_elbow_vec = elbow_pos - mid_point

mid_point_to_elbow_vec_scaled = mid_point_to_elbow_vec * 3

mid_point_to_elbow_point = mid_point + mid_point_to_elbow_vec_scaled

cmds.xform('pv',t=mid_point_to_elbow_point)