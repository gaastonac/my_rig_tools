#This tool is used to select the bones that affect a geometry
import maya.cmds as cmds
sel = cmds.ls(sl=True)
joints_skineados = cmds.skinCluster(q=True,inf='findRelatedSkinCluster')
cmds.select(joints_skineados)
