import random
import math
import csv

def random_roll(min,max):
    num = random.randint(min,max)
    return num

def asset_creator(regionNum,planets):
    #this function creats the planets ensure each plaent is unique and assigns values and assets randomly to each.
    #retuns the results as a list
    names = planetNames(regionNum, planets)
    planetList =[]
    for item in range(len(names)):
        planetList.append({
            "name": names[item],  # tlst holds the planet data before moving it here
            "vp": bonusVictoryPoints(),
            "location rewards": locRewards(),
            "Standard Objectives": objective_loader("standardObjectives.txt", 0, 2),
            "Campaign Objectives": objective_loader("campaignObjectives.txt", 0, 2),
            "Strategic Objectives": objective_loader("strategicObjectives.txt", 0, 2)
        })
    return planetList

def planetNames(regionNum,planets):
    #names to be expanded to 100 per region
    nameList=[]
    planetList=[]
    name=""
    count=0
    if regionNum == 1:
        nameList = file_loader("coreworlds.txt")
    if regionNum == 2:
        nameList = file_loader("innerrim.txt")
    if regionNum == 3:
        nameList = file_loader("midrim.txt")
    if regionNum == 4:
        nameList = file_loader("outerrim.txt")

    while count<=(planets)-1:
        name = nameList[random_roll(0, len(nameList) - 1)]
        if name in planetList:
            name = nameList[random_roll(0, len(nameList) - 1)]
        else:
            planetList.append(name)
            count+=1
    return planetList

def bonusVictoryPoints():
    num=random_roll(0,2)
    return num

def file_loader(filename):
    #finds the file. loads it strips the whitespace and outputs a s a basic list
    filenameList =[]
    fh = open(filename)
    for name in fh:
        name = name.strip()
        filenameList.append(name)
    fh.close()
    return filenameList

def map_coord ():
    #posistions are placeholder based on a 100x300 grid fo the moment
    position =[]
    xpos=random_roll(2,25)
    position.append(xpos)
    ypos=random_roll(2,18)
    position.append(ypos)
    return position

def map_position(planetList,planets):
    count = 0
    map_pos = []
    newLst = []
    for each in range(planets):
        while count<=(planets)-1:
            coOrd = map_coord()
            if coOrd in map_pos:
                coOrd = map_coord()
            else:
                coOrd[0] = coOrd[0]*40
                coOrd[1] = coOrd[1]*40
                map_pos.append(coOrd)
                count+=1

    for i in zip(planetList,map_pos):
        newLst.append(i)
    return newLst

def objective_loader(filename,min,max):
    objectives = random_roll(min, max)
    lstObj = file_loader(filename)
    lst = []
    count=0
    while count <= objectives - 1:
        resource = lstObj[random_roll(0, len(lstObj) - 1)]
        if resource in lst:
            resource = lstObj[random_roll(0, len(lstObj) - 1)]
        else:
            lst.append(resource)
            count += 1
    return lst

def locRewards():
    filename= "locRe.txt"
    lr=random_roll(0,2)
    #works not elegant
    diceroll = random_roll(1,5)
    value =""
    count=0
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
    lst=[]
    lstObj = file_loader(filename)#gets the name

    for item in range(0, lr):
            while count <= lr-1:
                resource = {lstObj[random_roll(0, len(lstObj) - 1)]:value}
                if resource in lst:
                    resource = {lstObj[random_roll(0, len(lstObj) - 1)]:value}
                else:
                    lst.append(resource)
                    count += 1

    return lst

def fleet_breakdown(fleet):
    fighter = math.ceil(fleet / 3)
    ship =  fleet - fighter
    print("fleet : ",fleet)
    print("Maximum points spent on ships : ", ship)
    print("Maximum points spent on fighters : ", fighter)

def num_planets(p):
  p = int(math.ceil(p*3.75)+1)
  return p

###### validators TXT version######
def region_check(message):
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

def player_check(message):
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

def fleet_check(message):
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

def callback(input):
    if input.isdigit():
        return True

    elif input is "":
        return True
    else:
        return False