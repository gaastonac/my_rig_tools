import maya.cmds as cmds
import math

def guides(guide_pelvis = 'Guide_Pelvis',guide_chest = 'Guide_Chest' ):
    locator_pelvis = cmds.spaceLocator(p=[0,0,0],n=guide_pelvis)

    cmds.group(n='grp_{}'.format(guide_pelvis))

    locator_chest = cmds.spaceLocator(p=[0, 0, 0], n=guide_chest)

    cmds.group(n='grp_{}'.format(guide_chest))

    cmds.select(cl=True)

    cmds.aimConstraint(locator_chest,locator_pelvis,w=1,aim=(0,1,0),u=(0,0,1),wu=(0,0,1),wut='vector')

def create_nurb():

    global nrb_spine
    global cvs_nurb

    scale_nurb = distance_between_guides()
    print scale_nurb
    nrb_spine = cmds.nurbsPlane(n='M_Spine_Nrb',p=(0,0,0),ax=(0,0,1),w=scale_nurb,lr=.1,d=3,u=2,v=1,ch=0)[0]

    cmds.rebuildSurface(nrb_spine,ch=0,rpo=1,rt=0,end=1,kr=0,kcp=0,kc=0,su=2,du=3,sv=1,dv=1,fr=0,dir=2)

    cmds.setAttr('{}.dispCV'.format(nrb_spine),1)

    cvs_nurb = cmds.getAttr('{}.cp'.format(nrb_spine),s=1)

    cmds.rotate(-90,'{}.cv[0:{}]'.format(nrb_spine,cvs_nurb-1),r=True,p=(0,0,0),os=True,z=True)

def build_setup():

    create_nurb()

    mid_position_guides = []

    position_chest = get_position_guides('Guide_Chest')

    position_pelvis = get_position_guides('Guide_Pelvis')

    for i in range (len(position_chest)):

        mid_position_guides.append((position_chest[i] + position_pelvis[i])/2)

    rotation_aim_pelvis = get_rotation_guides('Guide_Pelvis')

    print rotation_aim_pelvis

    #for i,xyz in enumerate (['X','Y','Z']):

        #cmds.setAttr('{}.rotate{}'.format(nrb_spine,xyz),rotation_aim_pelvis[i])

    cmds.move(mid_position_guides[0], mid_position_guides[1], mid_position_guides[2],
              '{}.cv[0:{}]'.format(nrb_spine, cvs_nurb - 1), r=True)

    cmds.rotate(rotation_aim_pelvis[0],rotation_aim_pelvis[1],rotation_aim_pelvis[2],
                '{}.cv[0:{}]'.format(nrb_spine, cvs_nurb - 1),
                p=(mid_position_guides[0],mid_position_guides[1],mid_position_guides[2]),
                os=True)

def distance_between_guides():

    point_1_coord = get_position_guides('Guide_Pelvis')

    point_2_coord = get_position_guides('Guide_Chest')

    # ecuacion de la recta d(a,b) = ?((x2-x1)**2) + (y2-=y1)**2) + (z2-z1)**2)

    x_result = (point_2_coord[0] - point_1_coord[0]) ** 2

    y_result = (point_2_coord[1] - point_1_coord[1]) ** 2

    z_result = (point_2_coord[2] - point_1_coord[2]) ** 2

    sum_values = x_result + y_result + z_result

    square_root_result = math.sqrt(sum_values)

    return square_root_result

def get_position_guides(point):

    position_coord = cmds.xform(point, ws=True, q=True, t=True)

    return position_coord

def get_rotation_guides(point):

    rotation_coord = cmds.xform(point, ws=True, q=True, ro=True)

    return rotation_coord

#guides()
build_setup()