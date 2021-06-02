import csv
import SWACG
###### classes and functions #######
def planet_cards(assetLst):
    for e in range(len(assetLst)):
      print ("\nplanet name : ",assetLst[e][0]["name"])
      print ("VP : ",assetLst[e][0]["vp"])
      print ("Location rewards :")
      for i in range (len(assetLst[e][0]["location rewards"])):
        for k,v in assetLst[e][0]["location rewards"][i].items():
          print("\t",k,":",v)
      print ("Standard Objective cards :")
      for i in range (len(assetLst[e][0]["Standard Objectives"])):
        print ("\t",assetLst[e][0]["Standard Objectives"][i])
      print ("Campaign Objectives cards :")
      for i in range (len(assetLst[e][0]["Campaign Objectives"])):
        print ("\t",assetLst[e][0]["Campaign Objectives"][i])
      print ("Strategic objective cards :")
      for i in range (len(assetLst[e][0]["Strategic Objectives"])):
        print ("\t",assetLst[e][0]["Strategic Objectives"][i])


###### main body #######
campaignName = input("sector name : ")
regionNum = 0
region = SWACG.region_check(" which region is the campaign to be set in?\n"
               "1. Core Worlds\n"
               "2. Inner Rim\n"
               "3. Mid Rim\n"
               "4. Outer Territories\n"
               "\tchoose option 1 to 4:")
if region == 1:
    region = "Core Worlds"
    regionNum = 1
elif region == 2:
    region = "inner Rim"
    regionNum = 2
elif region == 3:
    region = " Mid Rim"
    regionNum = 3
else:
    region = "outer Territories"
    regionNum = 4

numOfPlayers = SWACG.player_check(" number of players between 2 and 8: ")

numOfPlanets = SWACG.num_planets(numOfPlayers)
#tradeRoutes = 0 #placeholder var not yet in use
fleetSize = SWACG.fleet_check("size of each players fleet? (200 recommended) :")

print("\nsector name:",campaignName, "\nRegion:",region,"\nNumber of players:",numOfPlayers,"\nPlanets to generate:",numOfPlanets)
print(SWACG.fleet_breakdown(fleetSize))

p_lst = SWACG.asset_creator(regionNum,numOfPlanets)
print(len(p_lst))
l_lst = SWACG.map_position(p_lst,numOfPlanets)
print()

planet_cards(l_lst)
print()
for i in l_lst:
    print(i)

"""
#no visible outcome
while True:
    rewritemapCoord = input("change map positions Y/N? ").lower()
    if rewritemapCoord =="y":
        assetLst = SWACG.map_position(planet_assets,numOfPlanets)
        planet_cards(assetLst)
    else:
        break
print()
"""
while True:
    reset_planets = input("reset planets Y/N ?").lower()
    if reset_planets == "y":
        p_lst = SWACG.asset_creator(regionNum, numOfPlanets)
        l_lst = SWACG.map_position(p_lst, numOfPlanets)
        planet_cards(l_lst)
    else:
        break
print()

writeCSV=input("save as a csv Y/N? ").lower()

if writeCSV=="y":
    with open('planet_assets.csv', 'w',newline="") as f:
        assetWriter = csv.writer(f)
        assetWriter.writerow(["sector name :",campaignName])
        assetWriter.writerow(("number of players :",numOfPlayers))
        assetWriter.writerow(["Region :", region])
        assetWriter.writerow(["number of planets :",numOfPlanets])
        assetWriter.writerow(["Fleet Size :",fleetSize])
        for item in (p_lst):
            assetWriter.writerow([item])