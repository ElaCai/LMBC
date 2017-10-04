import random
import matplotlib.pyplot as plt
debug=False
#init results list
results=[]

def animals(results):
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
    if debug:print("Remaining animal number=",len(totalGroup))
    if debug:print("Final list=",str(totalGroup))
    if debug:print("Combined count=",combinedCount)
    results.append(len(totalGroup))

tries=10000
for j in range (0,tries):
    animals(results)
print(results)
X=[]
Y=[]
#Count
resultsSet=set(results)
for item in resultsSet:
    print(item, 'count=',results.count(item))
    X.append(item)
    Y.append(results.count(item))
plt.bar(X,Y,0.4,color="green")
plt.xlabel("# of remaining Feng")  
plt.ylabel("Frequency")
plt.title("Statistics of "+str(tries)+" tries")
for a,b in zip(X,Y):    
 plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=11) 
plt.show()
