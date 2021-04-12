import random
import math
import csv
# TODO
# DONEadd data for objective cards
# DONE create the local rewards function 
# DONE start on asset creator function 
# DONE start validation
# DONE start creating modules
# DONE breakdown of fleet assets per player
# DONE output MVP to csv 
# output MVP to html
# DONE reroll MVP with same values'
# DONE reroll MVP with new positions values
# look into converting over to json
# DONE strip co ord out of asset creator and have it in its own function
# add validation to objective functions (duplicates)
# tkinter
# DONE canvas with random/playerselect bg image
# DONE canvas add planets to canvas with names
# DONE save canvas as a png // hardcoded ONLY 
# add tabs, tab 1 suer input +map, tab 2 cards for map, tab 3 object cards used?
# menu system. save, load(?) about nothing more
# add dropdowns where relevant

def randomRoll(min,max):
    num = random.randint(min,max)
    return num

def assetCreator(regionNum,numOfPlanets):
    #this function creats the planets ensure each plaent is unique and assigns values and assets randomly to each.
    #retuns the results as a (overly complex) list
    tmpList = planetNames(regionNum, numOfPlanets)
    planetList =[]
    # streamline the for loop below?
    for item in tmpList:
        planetList = []
        for item in range(0, len(tmpList)):
            planetList.append({
                "name": tmpList[item],  # tmp list holds the planet data before moving it here
                "vp": bonusVictoryPoints(),
                "location rewards": locRewards(),
                "Standard Objectives cards": objectiveLoader("standardObjectives.txt", 0, 2),
                "Campaign Objectives": objectiveLoader("campaignObjectives.txt", 0, 2),
                "Strategic objectives": objectiveLoader("strategicObjectives.txt", 0, 2)
            })

    return planetList

def planetNames(regionNum,numOfPlanets):
    #names to be expanded to 100 max per region if possible
    nameList=[]
    planetList=[]
    name=""
    count=0
    if regionNum == 1:
        nameList = fileLoader("coreworlds.txt")
    if regionNum == 2:
        nameList = fileLoader("innerrim.txt")
    if regionNum == 3:
        nameList = fileLoader("midrim.txt")
    if regionNum == 4:
        nameList = fileLoader("outerrim.txt")

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
    #finds the file. loads it, strips the whitespace and outputs a s a basic list
    filenameList =[]
    fh = open(filename)
    for name in fh:
        name = name.strip()
        filenameList.append(name)
    fh.close()
    return filenameList

def mapCoOrd ():
    #determins coordinates based on x y px with a 100px deadzone
    position =[]
    xpos=randomRoll(100,1400)
    position.append(xpos)
    ypos=randomRoll(100,500)
    position.append(ypos)
    return position

def objectiveLoader(filename,min,max):
    objectives = randomRoll(min, max)
    lst = []
    lstObj = fileLoader(filename)
    for item in range(0, objectives):
        lst.append(lstObj[randomRoll(0,len(lstObj)-1)])
    return lst

def locRewards():
    filename="temptest.txt"
    lr=randomRoll(1,2)
    #works not elegant
    diceroll = randomRoll(1,5)
    value =""
    if diceroll ==1:
        value="8/4"
    if diceroll == 2:
        value = "10/5"
    if diceroll ==3:
        value = "12/6"
    if diceroll ==4:
        value = "24/12"
    if diceroll ==5:
        value = "30/15"
    lst =[]
    lstObj = fileLoader(filename)
    for item in range(0, lr):
        lst.append({lstObj[randomRoll(0, len(lstObj) - 1)]:value})

# listed upgrades / with possible values
# Offensive Retrofit 10/5
# Defensive Retrofit 10/5
# Support Team 10/5 8/4
# Officer 8/4 10/5
# Title 10/5 12/6 8/4
# Ordnance 10/5 12/6
# Fleet Command 8/4
# Ion Cannons 8/4 10/5
# Turbolasers 10/5
# Experimental Retrofits 8/4
# Squadron24/12 30/15
# Weapons Team 10/5
# Fleet Support 8/4
    return lst

def fleetBreakdown(fleetSize=200):
    fighter = math.ceil(fleetSize / 3)
    ship =  fleetSize - fighter
    print("fleetsize : ",fleetSize)
    print("Maximum points spent on ships : ", ship)
    print("Maximum points spent on fighters : ", fighter)

def mapPosition(planetList,numOfPlanets):
    count = 0
    mapPos =[]
    newLst=[]
    for each in range(numOfPlanets):
        while count<=(numOfPlanets)-1:
            coOrd = mapCoOrd()
            if coOrd in mapPos:
                coOrd = mapCoOrd()
            else:
                mapPos.append(coOrd)
                count+=1

    for i in zip(planetList,mapPos):
        newLst.append(i)

    return newLst

###### validators ######
def regionCheck(message):
  while True:
    try:
      message = int(input(message))
      if message <= 0 or message >4:
        message ='You must enter a valid number only : '
        continue

      else:
        return message
    except:
      message ='You must enter a valid number only : '

def playerCheck(message):
    while True:
        try:
            message = int(input(message))
            if message <2 or message > 8:
                message = 'You must enter a valid number only : '
                continue

            else:
                return message
        except:
            message = 'You must enter a valid number only : '

def fleetCheck(message):
    while True:
        try:
            message = int(input(message))
            if message <0:
                message = 'You must enter a valid number only : '
                continue

            else:
                return message
        except:
            message = 'You must enter a valid number only : '
            
