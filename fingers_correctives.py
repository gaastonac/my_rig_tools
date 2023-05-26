import maya.cmds as cmds

fingers = ['Index','Middle','Ring','Pinky','Thumb']
num = 1
for finger in fingers:
    for num in range(1,4):
        cmds.setAttr('P_L_'+finger+'_0'+str(num)+'_Corrective_Right_CTL.translateY',0)

        cmds.disconnectAttr('RV_Loc_L_'+finger+'_0'+str(num)+'_Corrective_Right.outValue',
                            'Z_L_'+finger+'_0'+str(num)+'_Corrective_Right_CTL.translateZ')

        cmds.setAttr('RV_Loc_L_'+finger+'_0'+str(num)+'_Corrective_Right.outputMax',1)

        cmds.connectAttr('RV_Loc_L_' + finger + '_0' + str(num) + '_Corrective_Right.outValue',
                            'Z_L_' + finger + '_0' + str(num) + '_Corrective_Right_CTL.scaleZ')

        num = num + 1
