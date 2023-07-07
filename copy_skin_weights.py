#This tool is used to select the bones that affect a geometry
import maya.cmds as cmds
geo_with_skin = cmds.ls(sl=True)[0]
geo_target = cmds.ls(sl=True)[1]
joints_skineados = cmds.skinCluster(geo_with_skin,q=True,inf='findRelatedSkinCluster')


cmds.skinCluster( joints_skineados, geo_target,bm=0,sm=0,nw=1,wd=0,mi=5,omi=False)
cmds.copySkinWeights(geo_with_skin,geo_target,nm=True, sa='closestPoint',ia='oneToOne')

