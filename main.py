#option selection
import random
def randomRoll(min,max):
    num = random.randint(min,max)
    return num

def bonusVictoryPoints():
    num=randomRoll(0,2)
    return num

def mapPosition ():
    #posistions are placeholder based on a 10x10 grid fo the moment
    position =[]
    xpos=randomRoll(0,10)
    position.append(xpos)
    ypos=randomRoll(0,10)
    position.append(ypos)
    return position

def planetNames(regionNum,numOfPlanets):
    nameList=[]
    planetList=[]
    name=""
    count=0
    if regionNum == 1:
        nameList = ["Ambria","Amethia Prime","Antar","Arreyel","Bastatha","Bernilla","Bestine IV","Birren","Calcoraan","Chaaktil"]
    if regionNum == 2:
        nameList = ["Champala","Colla IV","Cona","Denon","Dwartii","Gilvaanen","Gorse","Guagenia","Kiffex","Kiffu"]
    if regionNum == 3:
        nameList = ["Kooriva","Li-Toran","Manaan","Navlaas","Obroa-skai","Onderon","Orchis","Pasher","Phateem","Pheryon"]
    if regionNum == 4:
        nameList = ["Pijal","Quarzite","Riosa","Sergia","Taanab","Telerath","Throffdon","Ubduria","Vurdon Ka","Xibariz"]

    while count<=(numOfPlanets)-1:
        name = nameList[randomRoll(0, len(nameList) - 1)]
        if name in planetList:
            name = nameList[randomRoll(0, len(nameList) - 1)]
        else:
            planetList.append(name)
            count+=1
    return planetList

#***** main body *****
campaignName = input("sector name : ")
regionNum = 0
region = input(" which region is the campaign to be set in?\n"
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

numOfPlayers = int(input(" number of players between 2 and 8: "))
numOfPlanets = int((numOfPlayers)+1) #true formula (numofplayer*4)+1)
tradeRouts = 0 #placeholder var

print("\nsector name:",campaignName, "\nRegion:",region,"\nNumber of players:",numOfPlayers,"\nPlanets to generate:",numOfPlanets)
tmpList=planetNames(regionNum,numOfPlanets)

#streamline the for loop below
for item in tmpList:
    planetList=[]
    for item in range(0,len(tmpList)):
        planetList.append({
            "id":item+1,
            "name":tmpList[item],
            "vp":bonusVictoryPoints(),
            "location rewards": "place holder list of 2 max",
            "Strategic objectives": "place holder list of 2 max",
            "Standard Objectives": "place holderlist of 2 max",
            "Campaign Objectives": "place holder list of 2 max",
            "map position": mapPosition()
        })

for item in planetList:
    print(item)
