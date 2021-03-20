import random

#20/03/2021 TODO
# add data for objective cards
# create the local rewards function
# start on asset creator function
# start validation

def randomRoll(min,max):
    num = random.randint(min,max)
    return num

def assetCreator():
    return False

def planetNames(regionNum,numOfPlanets):
    #names to be expanded to 100 per region
    nameList=[]
    planetList=[]
    name=""
    count=0
    #core worlds code ver1
    if regionNum == 1:
       nameList = ["Abregado-rae","Alsakan","Anaxes","Athulla","Balosar","Bar'leth","Botor","Brentaal IV","Cardota",
            "Cavas","Chandrila","Corellia","Corulag","Coruscant","Courtsilius","Davnar II","Dowut","Duro","Fedalle",
            "Ganthel","Gatalenta","Grizmallt","Harloff Minor","Hosnian Prime","Humbarine","Kuat","Lanz Carpo","Lespectus",
            "Metellos","N'Zoth","Neral","Pillio","Plexis","Ralltiir","Raysho","Salliche","Selonia","Sissubo","Skako",
            "Talus","Tangenine","Tepasi","Tinnel IV","Tralus","Vardos"]
    #inner rim code ver 2
    if regionNum == 2:
        fh=open("innerrim.txt")
        for name in fh:
            name=name.strip()
            nameList.append(name)
        #nameList = ["Champala","Colla IV","Cona","Denon","Dwartii","Gilvaanen","Gorse","Guagenia","Kiffex","Kiffu"]
    #midrim code ver 3
    if regionNum == 3:
        nameList = fileLoader("midrim.txt")
        #["Kooriva","Li-Toran","Manaan","Navlaas","Obroa-skai","Onderon","Orchis","Pasher","Phateem","Pheryon"]
    #outer rim test version
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

def bonusVictoryPoints():
    num=randomRoll(0,2)
    return num

def fileLoader(filename):
    #finds the file. loads it strips the whitespace and outputs a s a basic list
    filenameList =[]
    fh = open(filename)
    for name in fh:
        name = name.strip()
        filenameList.append(name)
    return filenameList

def mapPosition ():
    #posistions are placeholder based on a 10x10 grid fo the moment
    position =[]
    xpos=randomRoll(0,10)
    position.append(xpos)
    ypos=randomRoll(0,10)
    position.append(ypos)
    return position

def objectiveLoader(filename):
    objectives = randomRoll(0, 2)
    lst = []
    lstObj = fileLoader(filename)
    #test list
    # ["Resources", "Skilled Spacers", "Repair Yards", "Spynet", "Destiny"]
    for item in range(0, objectives):
        lst.append(lstObj[randomRoll(0,len(lstObj)-1)])
    return lst

def locRewards():
    return False

###### validators ######
def inputCheck(message):
  while True:
    try:
      message = int(input(message))
      if message<= 0:
        message ='You must enter a valid number : '
        continue
      else:
        return message
    except:
      message ='You must enter a valid number : '

###### main body #######
campaignName = input("sector name : ")
regionNum = 0
region = int(input(" which region is the campaign to be set in?\n"
               "1. Core Worlds\n"
               "2. Inner Rim\n"
               "3. Mid Rim\n"
               "4. Outer Territories\n"
               "\tchoose option 1 to 4:"))
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

numOfPlayers = input(" number of players between 2 and 8: ")
numOfPlanets = int(numOfPlayers)+1 #true formula (numofplayer*4)+1)
tradeRouts = 0 #placeholder var

print("\nsector name:",campaignName, "\nRegion:",region,"\nNumber of players:",numOfPlayers,"\nPlanets to generate:",numOfPlanets)
tmpList=planetNames(regionNum,numOfPlanets)

#streamline the for loop below
for item in tmpList:
    planetList=[]
    for item in range(0,len(tmpList)):
        planetList.append(item+1)
        planetList.append({
            "name":tmpList[item],
            "vp":bonusVictoryPoints(),
            "location rewards": locRewards(),
            "Standard Objectives cards": objectiveLoader("standardObjectives.txt"),
            "Campaign Objectives": objectiveLoader("campaignObjectives.txt"),
            "Strategic objectives": objectiveLoader("standardObjectives.txt"),
            "map position": mapPosition()
        })

for entry in planetList:
    print(entry)




