import maya.cmds as cmds

# Make a new window
if cmds.window("Create Ctrl", exists=True):
    cmds.deleteUI("Create Ctrl")
window = cmds.window("Create Ctrl", title="Create Ctrl", iconName='Short Name', s=False, widthHeight=(300, 150))
cmds.columnLayout(adjustableColumn=True)
cmds.separator(height=10, style='double')
cmds.text('Create by. Gaastonac')
cmds.separator(height=10, style='double')
radio = cmds.intSliderGrp(l="Radio", min=1, max=100, f=True, value=1)
Orient = cmds.checkBox(label='Orient Constraint')
Parentc = cmds.checkBox(label='Parent Constraint')
cmds.button(label='Create', command=('ctrl()'), h=50)
cmds.showWindow(window)


def ctrl():
    sel = cmds.ls(selection=True)
    lsel = len(sel)
    print sel, lsel

    if lsel == 0:
        myfinalradio = cmds.intSliderGrp(radio, q=True, v=True)
        ctrl_World = cmds.circle(nr=(0, 1, 0), n=("Ctrl_"), r=myfinalradio)
        zgroup = cmds.group(n=("Z_Ctrl_"), em=True)
        pgroup = cmds.group(n=("P_Ctrl_"), em=True)
        grupo_control = cmds.parent(ctrl_World, zgroup)
        grupo_grupo_control = cmds.parent(zgroup, pgroup)
        print ctrl_World
    for bone in range(lsel):
        checkboxOrient = cmds.checkBox(Orient, q=True, v=True)
        checkboxParent = cmds.checkBox(Parentc, q=True, v=True)
        print checkboxOrient
        print checkboxParent
        if checkboxOrient == True:
            translate = cmds.xform(sel[bone], ws=True, q=True, t=True)
            rot = cmds.xform(sel[bone], ws=True, q=True, ro=True)
            radio_ctrl = cmds.getAttr(sel[bone] + ".radius")
            print radio
            myfinalradio = cmds.intSliderGrp(radio, q=True, v=True)
            ctrl = cmds.circle(n=("Ctrl_" + sel[bone]), nr=(1, 0, 0), r=myfinalradio)
            zgroup = cmds.group(n=("Z_Ctrl_" + sel[bone]))
            pgroup = cmds.group(n=("P_Ctrl_" + sel[bone]))
            emparentarTrans = cmds.xform(pgroup, ws=True, t=translate)
            emparentarRot = cmds.xform(pgroup, ws=True, ro=rot)
            cmds.orientConstraint(ctrl, sel[bone])

        if checkboxParent == True:
            translate = cmds.xform(sel[bone], ws=True, q=True, t=True)
            rot = cmds.xform(sel[bone], ws=True, q=True, ro=True)
            radio_ctrl = cmds.getAttr(sel[bone] + ".radius")
            print radio
            myfinalradio = cmds.intSliderGrp(radio, q=True, v=True)
            ctrl = cmds.circle(n=("Ctrl_" + sel[bone]), nr=(1, 0, 0), r=myfinalradio)
            zgroup = cmds.group(n=("Z_Ctrl_" + sel[bone]))
            pgroup = cmds.group(n=("P_Ctrl_" + sel[bone]))
            emparentarTrans = cmds.xform(pgroup, ws=True, t=translate)
            emparentarRot = cmds.xform(pgroup, ws=True, ro=rot)
            cmds.parentConstraint(ctrl, sel[bone])
