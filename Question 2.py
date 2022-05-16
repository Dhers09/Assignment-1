import matplotlib.pyplot as plt
myNumbers = []
n =""

def is_float (n):             #tries to convert input to float, if possible returns True, if False overlooks error and continues code
        try :             
            float (n)         #eq1. if n = 6 returns True
            return True       #eq2. if n = 'p' returns False. Same for any non numeric string
        except ValueError :
            return False
        
while not n == "*":
    n = input("Please input numbers and * only at the end to stop: ")
    print(type(n))
    if is_float(n):
        myNumbers.append(float(n))
    else:
        print("Cannot be converted to float")
    
mean = sum(myNumbers)/len(myNumbers)
print("Mean = ", mean)

myNumbers.sort()
if len(myNumbers) % 2 == 1:      #checks if odd amount of numbers
    pos = len(myNumbers)//2      #finds middle position and rounds down
    print("Median = ", myNumbers[pos])
   
elif len(myNumbers) % 2 == 0:    #checks if evenamount of numbers
    pos = len(myNumbers)//2      
    avg_pos = (myNumbers[pos] + myNumbers[pos - 1])/2     #adds 2 middle values and finds average
    print("Median = ", avg_pos)

s = 0
for x in myNumbers:
    eq1 = ((x - mean)**2)/len(myNumbers)      #eq1 is standard deviation before square root & summation
    s = s + eq1
    
std_dev = s **0.5
print("Standard Deviation = ", std_dev)
plt.xlabel("Entered values")
plt.ylabel("Frequency of numbers")
plt.hist(myNumbers, bins=range(len(myNumbers)+1),ec="k")  #bins have = range of a set of values + 1, ec="k" is for the defining lines
plt.show()