import easygui
import math
#Test case. Change the number here and run to see different results
#allow user to input an interger [2,100000]
n=easygui.integerbox("Please input the n of Egyptian Fraction 1/n...",lowerbound=2,upperbound=100000)

print ("Divide Egyptian Fraction (",n,") into sum of 3 smaller Egyptian Factions...")
count=0

a=0
b=0
c=0
for a in range (n+1, n*3+1):
    for b in range (math.ceil(a*n/(a-n)),math.floor(2*a*n/(a-n)+1)):
        if(a*b-b*n-a*n)!=0:
            c=(a*b*n)/(a*b-b*n-a*n)
            count=count+1
            print ("Combination",count,"= 1/",int(a),"+1/",int(b),"+1/",int(c))

                  

