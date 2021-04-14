#testing only
#updated main code to prevent repeats

lst=[({'name': 'Ringo Vinda', 'vp': 2, 'location rewards': [{'Fleet Support': '10/5'}], 'Standard Objectives cards': ['Superior Positions', 'Superior Positions'], 'Campaign Objectives': [], 'Strategic objectives': ['Ally', 'Repair yards']}, [180, 168]),
({'name': 'Ando', 'vp': 2, 'location rewards': [{'Fleet Support': '24/12'}, {'Ordnance': '24/12'}], 'Standard Objectives cards': [], 'Campaign Objectives': ['Hired Scum'], 'Strategic objectives': []}, [229, 200]),
({'name': 'Cyphar', 'vp': 0, 'location rewards': [{'Squadron': '8/4'}, {'Offensive Retrofit': '8/4'}], 'Standard Objectives cards': ['Superior Positions'], 'Campaign Objectives': ['Double Agents'], 'Strategic objectives': ['Resources', 'Ally']}, [249, 249]),
({'name': 'Aleen Minor', 'vp': 2, 'location rewards': [{'Squadron': '10/5'}], 'Standard Objectives cards': ['Marked for Destruction'], 'Campaign Objectives': ['Prototype Recovery', 'Prototype Recovery'], 'Strategic objectives': []}, [146, 120]),
({'name': 'Bardelberan 7', 'vp': 0, 'location rewards': [{'Fleet Support': '30/15'}, {'Turbolasers': '30/15'}], 'Standard Objectives cards': [], 'Campaign Objectives': ['Hired Scum', 'Steel Supplies'], 'Strategic objectives': ['Repair yards', 'Ally']}, [281, 169])]

#print(lst[1][0]["location rewards"])

for e in range(len(lst)):
  print ("\nplanet name : ",lst[e][0]["name"])
  print ("VP : ",lst[e][0]["vp"])
  print ("Location rewards :")
  for i in range (len(lst[e][0]["location rewards"])):
    print ("\t",lst[e][0]["location rewards"][i])
  print ("Standard Objective cards :")
  for i in range (len(lst[e][0]["Standard Objectives cards"])):
    print ("\t",lst[e][0]["Standard Objectives cards"][i])
  print ("Campaign Objectives cards :")
  for i in range (len(lst[e][0]["Campaign Objectives"])):
    print ("\t",lst[e][0]["Campaign Objectives"][i])
  print ("Strategic objective cards :")
  for i in range (len(lst[e][0]["Strategic objectives"])):
    print ("\t",lst[e][0]["Strategic objectives"][i])      
