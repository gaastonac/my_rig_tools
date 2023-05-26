import json
with open(r'E:\joints_data.json') as file:
    data = json.load(file)
    for j in data['joints']:
       
       name_j = j.get('name')
       
       translateX = j.get('translateX')
       translateY = j.get('translateY')
       translateZ = j.get('translateZ')
       
       radius = j.get('radius')
       
       createJoint= cmds.joint(n=j.get('name'),r=1)
       
       cmds.setAttr('{}.translateX'.format(createJoint),translateX)
       
       cmds.setAttr('{}.translateY'.format(createJoint),translateY)
       
       cmds.setAttr('{}.translateZ'.format(createJoint),translateZ)
       
       cmds.setAttr('{}.radius'.format(createJoint),radius)
       
       cmds.select(cl=True)

########################################################################
import json
sel = cmds.ls(sl=True)

data = {}
data['joints'] = []
for j in sel:
    data['joints'].append({
        'name':j,
        'translateX':cmds.getAttr('{}.translateX'.format(j)),
        'translateY':cmds.getAttr('{}.translateY'.format(j)),
        'translateZ':cmds.getAttr('{}.translateZ'.format(j)),
        'radius':cmds.getAttr('{}.radius'.format(j))})

print data

with open(r'E:\joints_data.json', 'w') as file:
    json.dump(data, file, sort_keys=True,indent=4)
