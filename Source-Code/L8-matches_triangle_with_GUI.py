import math,easygui,turtle,random
#Debug switch
debug=False
#Get user input. Validate input is an interger in the range [3,100000]
n=easygui.integerbox("Please input your total matches number[3,100000]",
                     lowerbound=3,
                     upperbound=100000)
if debug: print ("Total matches=",n)

#Calculate
totalTricount=0
isoscelesTriCount=0
rightAngleTriCount=0
obtuseTriCount=0
acuteTriCount=0
triList=[]
for a in range (int((n+2)/3),int(((n-1)/2)+1)+1):
    for b in range (1,int(n-1/2)+1):
        c=n-a-b
        if c<=a and c<=b and b<=a and b+c>a:
            totalTricount=totalTricount+1
            if a**2==b**2+c**2:
                rightAngleTriCount=rightAngleTriCount+1
                if debug:print (a,b,c)
            elif a**2>b**2+c**2:
                obtuseTriCount=obtuseTriCount+1
            elif a**2<b**2+c**2:
                acuteTriCount=acuteTriCount+1
            elif a==b or b==c or a==c:
                isoscelesTriCount=isoscelesTriCount+1
                if debug:print (a,b,c)
            triList.append([a,b,c])

#Print result to GUI
easygui.textbox(msg="QUESTION\nUse "+
                str(n)+
                " matches to form triangles. How many can you get?",
                title="Result",
                text="ANSWER\n"+"(1)Total triange="+str(totalTricount)+
                "\n(2)Isosceles triange="+str(isoscelesTriCount)+
                "\n(3)Right-angle triange="+str(rightAngleTriCount)+
                "\n(4)Obtuse-angle triange="+str(obtuseTriCount)+
                "\n(5)Acute-angle triange="+str(acuteTriCount),
                codebox=True)

# Draw triangle
t = turtle.Pen()
t.down()
t.speed(0)
turtle.bgcolor("black")
colors=["blue","green","orange","red","yellow","white","purple","brown"]
for i in range (0,len(triList)):
    tri=triList[i]
    abDegree=math.degrees(math.acos((tri[0]**2 + tri[1]**2 - tri[2]**2) / (2 * tri[0] * tri[1])))
    bcDegree=math.degrees(math.acos((tri[1]**2 + tri[2]**2 - tri[0]**2) / (2 * tri[1] * tri[2])))
    t.pencolor(colors[i%8])
    t.forward(int(tri[0])*2)
    t.right(180-int(abDegree))
    t.forward(int(tri[1])*2)
    t.right(180-int(bcDegree))
    t.forward(int(tri[2])*2)

