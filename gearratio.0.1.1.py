import math
chainring = int(input("What is the chain ring size?"))
cog = int(input("What is the cog size?"))
gearratio = chainring/cog
tiresize = int(input("What is the tire size?"))
wheel = int(input("What is the wheel size?"))
circum = (wheel+(tiresize*2))*math.pi
developement = (circum*gearratio)
print ("Your gear ratio is", gearratio)
print ("Your development is",developement,"mm")
