import easygui
#Test case. Change the number here and run to see different results
#n=27
#allow user to input an interger [2,100000]


n=easygui.integerbox("Please input the n of Egyptian Fraction 1/n...",lowerbound=2,upperbound=100000)

print ("Divide Egyptian Fraction (",n,") into sum of 2 smaller Egyptian Factions...")
count=0

for a in range (n+1, n*2+1):
    b=a*n/(a-n)
    if a*b%n==0:
        count+=1
        print ("Combination",count,"= 1/",int(a),"+1/",int(b))
        #plot(a,b)

print ("Divide Egyptian Fraction (",n,") into diff of 2 smaller Egyptian Factions...")
count=0

for a in range (1,n-1):
    b=a*n/(a-n)
    if a*b%n==0:
        count+=1
        print ("Combination ",count,"= 1/",int(a),"-1/",abs(int(b)))

#plot.show()


