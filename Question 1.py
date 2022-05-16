n=int(input("Please Input Any Number: "))
if n % 3 == 0 and n % 5 == 0:
    if n % 3 == 0 and n % 5 == 0 and n % 2 == 0:    #if n is divisible by 2,3 and 5
        print("kinPkcalB")
    else:
        print("BlackPink")
    
elif n % 3 == 0:
    if n % 3 == 0 and n % 2 == 0:                   #if n is divisible by 2 and 3
        print("kcalB")
    else:
         print("Black")
elif n % 5 == 0:
    if n % 5 == 0 and n % 2 == 0:                   #if n is divisible by 2 and 5
        print("kinP")
    else:
        print("Pink")
elif n % 2 == 0:
    print("Only divisible by 2")
else:
    print("Not divisible by 2,3 or 5") 