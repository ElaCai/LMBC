import random
debug=False
numOfDragon=100
numOfFeng=101
numOfHuang=102
groupDragon=["Dragon"]*numOfDragon
groupFeng=["Feng"]*numOfFeng
groupHuang=["Huang"]*numOfHuang
totalGroup=[]
totalGroup.extend(groupDragon)
totalGroup.extend(groupFeng)
totalGroup.extend(groupHuang)
species=["Dragon","Feng","Huang"]
random.shuffle(totalGroup)
if debug:print("Initial shuffled List\n",str(totalGroup))
newslice=[]
combinedCount=0
while len(set(species).difference(set(totalGroup)))<2:
    #Randomly select 2 elements and delete from previous list
    newslice=random.sample(totalGroup,2)
    for i in (0,1):
        try:
            totalGroup.remove(newslice[i])
        except ValueError:
            if debug:print("cannot find ",newslice[i])
            break
    if newslice[0]==newslice[1]:
        if debug:print("same animals:",str(newslice)," put back")
        #same animals. Put the slice back                                          
        totalGroup.extend(newslice)
    else:
        #This is the combined animal
        combinedAnimal=set(species).difference(set(newslice))
        combinedCount+=1
        if debug:print("Combined Animal=",combinedAnimal)
        totalGroup.extend(combinedAnimal)
print("Remaining animal number=",len(totalGroup))
print("Final list=",str(totalGroup))
print("Combined count=",combinedCount)

