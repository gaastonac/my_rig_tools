'''Script for create control in joint with constraint orient or parent'''

import maya.cmds as cmds

# Make a new window
if cmds.window('Create Ctrl', exists=True):
    
    cmds.deleteUI('Create Ctrl')
    
window = cmds.window('Create Ctrl', title='Create Ctrl', iconName='Short Name', s=False, widthHeight=(300, 150))

cmds.columnLayout(adjustableColumn=True)

cmds.separator(height=10, style='double')

cmds.text('Create by. Gaastonac')

cmds.separator(height=10, style='double')

radio = cmds.intSliderGrp(l='Radio', min=1, max=100, f=True, value=1)

Orient = cmds.checkBox(label='Orient Constraint')

parent_cons = cmds.checkBox(label='Parent Constraint')

cmds.button(label='Create', command=('ctrl()'), h=50)

cmds.showWindow(window)


def ctrl():
    sel = cmds.ls(selection=True)
    
    lsel = len(sel)


    if lsel == 0:
        
        myfinalradio = cmds.intSliderGrp(radio, q=True, v=True)
        
        ctrl_World = cmds.circle(nr=(0, 1, 0), n='Ctrl_', r=myfinalradio)
        
        zgroup = cmds.group(n='Z_Ctrl_', em=True)
        
        pgroup = cmds.group(n='P_Ctrl_', em=True)
        
        cmds.parent(ctrl_World, zgroup)
        
        cmds.parent(zgroup, pgroup)
        

    for bone in range(lsel):
        
        checkboxOrient = cmds.checkBox(Orient, q=True, v=True)
        
        checkboxParent = cmds.checkBox(parent_cons, q=True, v=True)
        
        if checkboxOrient == True:
            
            translate = cmds.xform(sel[bone], ws=True, q=True, t=True)
            
            rot = cmds.xform(sel[bone], ws=True, q=True, ro=True)
            
            cmds.getAttr('{}.radius'.format(sel[bone]))

            myfinalradio = cmds.intSliderGrp(radio, q=True, v=True)
            
            ctrl = cmds.circle(n='Ctrl_{}'.format(sel[bone]), nr=(1, 0, 0), r=myfinalradio)
            
            zgroup = cmds.group(n='Z_Ctrl_{}'.format(sel[bone]))
            
            pgroup = cmds.group(n='P_Ctrl_{}'.format(sel[bone]))
            
            cmds.xform(pgroup, ws=True, t=translate)
            
            cmds.xform(pgroup, ws=True, ro=rot)
            
            cmds.orientConstraint(ctrl, sel[bone])

        if checkboxParent == True:
            
            translate = cmds.xform(sel[bone], ws=True, q=True, t=True)
            
            rot = cmds.xform(sel[bone], ws=True, q=True, ro=True)
            
            cmds.getAttr('{}.radius'.format(sel[bone]))

            myfinalradio = cmds.intSliderGrp(radio, q=True, v=True)
            
            ctrl = cmds.circle(n='Ctrl_{}'.format(sel[bone]) , nr=(1, 0, 0), r=myfinalradio)
            
            zgroup = cmds.group(n='Z_Ctrl_{}'.format(sel[bone]))
            
            pgroup = cmds.group(n='P_Ctrl_{}'.format(sel[bone]))
            
            cmds.xform(pgroup, ws=True, t=translate)
            
            cmds.xform(pgroup, ws=True, ro=rot)
            
            cmds.parentConstraint(ctrl, sel[bone])
