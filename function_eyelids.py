list_edge_upper = [u'body_geo.e[12815]', u'body_geo.e[12817]', u'body_geo.e[12819]', u'body_geo.e[12821]',
                   u'body_geo.e[12823]', u'body_geo.e[12825]', u'body_geo.e[12827]', u'body_geo.e[12829]',
                   u'body_geo.e[12831]', u'body_geo.e[12833]', u'body_geo.e[12835]', u'body_geo.e[12837]',
                   u'body_geo.e[12839]', u'body_geo.e[12841]']


list_edge_lower = [u'body_geo.e[12811]', u'body_geo.e[12813]', u'body_geo.e[12842]', u'body_geo.e[12845]',
                   u'body_geo.e[12847]', u'body_geo.e[12848]', u'body_geo.e[12851]', u'body_geo.e[12853]',
                   u'body_geo.e[12855]', u'body_geo.e[12857]', u'body_geo.e[12859]', u'body_geo.e[12861]',
                   u'body_geo.e[12863]', u'body_geo.e[12864]']


def poly_edge_to_curve(prefix,up_or_dwn,list_edges):

    set_eyelid = cmds.sets(n='{}_Set_Eyelid{}_Selection'.format(prefix,up_or_dwn))

    cmds.select(list_edges)

    cmds.sets(add=set_eyelid)

    crv_high = cmds.polyToCurve(n='{}_Crv_Eyelid{}_High'.format(prefix,up_or_dwn),
                                form=0,
                                degree=1,
                                conformToSmoothMeshPreview=1,
                                ch=False)[0]

    cmds.select(cl=True)

    crv_low = cmds.duplicate(crv_high, n='{}_Crv_Eyelid{}_Low'.format(prefix,up_or_dwn))[0]

    cmds.rebuildCurve(crv_low, ch=False, rpo=True, rt=0, end=1, kr=0, kcp=False, kep=True, kt=False, s=4, d=3)
    
    cmds.select(cl=True)


poly_edge_to_curve('L','Up',list_edge_upper)
poly_edge_to_curve('L','Dwn',list_edge_lower)