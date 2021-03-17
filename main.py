#option selection
campaignName = input("sector name : ")
region = input(" which region is the campaign to be set in?\n"
               "1. Core Worlds\n"
               "2. Inner Rim\n"
               "3. Mid Rim\n"
               "4. Outer Territories\n"
               "\tchoose option 1 to 4:")
if region == 1:
    region = "Core Worlds"
elif region == 2:
    region = "inner Rim"
elif region == 3:
    region = " Mid Rim"
else:
    region = "outer Territories"
numOfPlayers = int(input(" number of players between 2 and 8: "))
numOfPlanets = (numOfPlayers*4)+1
print("\nsector name:",campaignName, "\nRegion:",region,"\nNumber of players:",numOfPlayers,"\nPlanets to generate:",numOfPlanets)
