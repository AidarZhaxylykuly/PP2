import json, mod
x=mod.x
y = json.loads(x)
print('''Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------''')
for i in range(len(y['imdata'])):
    if len(y['imdata'][i]['l1PhysIf']['attributes']["dn"])==42:
        print(y['imdata'][i]['l1PhysIf']['attributes']["dn"], ' '*28, y['imdata'][i]['l1PhysIf']['attributes']["fecMode"], '  ', y['imdata'][i]['l1PhysIf']['attributes']["mtu"])
    else:
        print(y['imdata'][i]['l1PhysIf']['attributes']["dn"], ' '*29, y['imdata'][i]['l1PhysIf']['attributes']["fecMode"], '  ', y['imdata'][i]['l1PhysIf']['attributes']["mtu"])