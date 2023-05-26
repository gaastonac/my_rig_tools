import maya.cmds as cmds
import math

point_1 = 'pelvis'
point_2 = 'chest'

point_1_coord = cmds.xform(point_1,ws=True,q=True,t=True)
point_2_coord = cmds.xform(point_2,ws=True,q=True,t=True)

#ecuacion de la recta d(a,b) = ?((x2-x1)**2) + (y2-=y1)**2) + (z2-z1)**2)

x_result = (point_2_coord[0] - point_1_coord[0]) ** 2

y_result = (point_2_coord[1] - point_1_coord[1]) ** 2

z_result = (point_2_coord[2] - point_1_coord[2]) ** 2

sum_values = x_result + y_result + z_result

square_root_result = math.sqrt(sum_values)

print square_root_result

''' for to get mid position in two points
lista3 = []

for i, value in enumerate(point_2_coord):
    lista3.append((point_2_coord[i] + point_1_coord[i])/2)

print(lista3)
'''