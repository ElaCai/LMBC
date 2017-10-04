import turtle,math,time
n=200
count=0
for a in range ((n+2)/3,(n-1)/2+1):
    for b in range (n+2)/3,(n-1)/2+1):
        for c in range (n+2)/3,(n-1)/2+1):
            if b+c>a:
                count=count+1
                #print (a,b,c)
print (count)                
#3 sides
#a=5
#b=4
#c=3
#calcuate the degrees
abDegree=math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b)))
bcDegree=math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
acDegree=math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
print (abDegree,bcDegree,acDegree)

# 调用turtle中的Pen函数创建画布
t = turtle.Pen()
t.down()

# Draw triangle
t.forward(a*50)
t.right(180-abDegree)
t.forward(b*50)
t.right(180-bcDegree)
t.forward(c*50)

