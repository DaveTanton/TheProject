import random
import math
import csv
import SWACG
###### temp functions and classes #######

###### main body #######
campaignName = input("sector name : ")
regionNum = 0
region = SWACG.regionCheck(" which region is the campaign to be set in?\n"
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

numOfPlayers = SWACG.playerCheck(" number of players between 2 and 8: ")
numOfPlanets = int(numOfPlayers)+1 #true formula (numofplayer*3.75)+1)(1stcampaign rules)(2nd campaign needs working out)(make into function)
tradeRoutes = 0 #placeholder var not yet in use
fleetSize = SWACG.fleetCheck("size of each players fleet? (200 recommended) :")

print("\nsector name:",campaignName, "\nRegion:",region,"\nNumber of players:",numOfPlayers,"\nPlanets to generate:",numOfPlanets)
print(SWACG.fleetBreakdown(fleetSize))
planetAssets = SWACG.assetCreator(regionNum,numOfPlanets)
assetLst = SWACG.mapPosition(planetAssets,numOfPlanets)
for entry in assetLst:
    print(entry)

print()

while True:
    rewritemapCoord = input("change map positions Y/N? ").lower()
    if rewritemapCoord =="y":
        assetLst = SWACG.mapPosition(planetAssets,numOfPlanets)
        for entry in assetLst:
            print(entry)
    else:
        break
print()

while True:
    resetPlanets = input("reset planets Y/N ?").lower()
    if resetPlanets == "y":
        planetAssets = SWACG.assetCreator(regionNum, numOfPlanets)
        assetLst = SWACG.mapPosition(planetAssets, numOfPlanets)
        for entry in assetLst:
            print(entry)
    else:
        break
print()

writeCSV=input("save as a csv Y/N? ").lower()

if writeCSV=="y":
    with open('planetassets.csv', 'w',newline="") as f:
        assetWriter = csv.writer(f)
        assetWriter.writerow(["sector name :",campaignName])
        assetWriter.writerow(("number of players :",numOfPlayers))
        assetWriter.writerow(["Region :", region])
        assetWriter.writerow(["number of planets :",numOfPlanets])
        assetWriter.writerow((["trade routes :",tradeRoutes]))
        assetWriter.writerow(["Fleet Size :",fleetSize])
        for item in (planetAssets):
            assetWriter.writerow([item])
