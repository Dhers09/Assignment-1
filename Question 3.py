import matplotlib.pyplot as plt

monthly_val1 = [100000]    #array to house monthly values
monthly_val2 = [100000]
monthly_val3 = [100000]
monthly_val4 = [100000]
monthly_val5 = [100000]
m = 1        #months
c = 0        #a counter
months = 0

while m<61:
    rem_val = monthly_val1[m-1] - 1000          #equations to work out monthly values
    new_val = rem_val + (rem_val*(6.5/1200))
    if new_val < 0 and c < 1:        #c makes sure that the value of m equates to months once to find the first negative
        months = m 
        c = c + 1
    else:
        monthly_val1.append(new_val)
        m = m + 1
print("Repayments in ", months//12, " years and ", months % 12, "months")

m = 1
c = 0
while m<61:
    rem_val = monthly_val2[m-1] - 2000
    new_val = rem_val + (rem_val*(6.5/1200))
    if new_val < 0 and c < 1:
        months = m 
        c = c + 1
    else:
        monthly_val2.append(new_val)
        m = m + 1
print("Repayments in ", months//12, " years and ", months % 12, "months") 

m = 1
c = 0

while m<61:
    rem_val = monthly_val3[m-1] - 3000
    new_val = rem_val + (rem_val*(6.5/1200))
    if new_val < 0 and c < 1:
        months = m 
        c = c + 1
    else:
        monthly_val3.append(new_val)
        m = m + 1
print("Repayments in ", months//12, " years and ", months % 12, "months")    

m = 1
c=0

while m<61:
    rem_val = monthly_val4[m-1] - 4000
    new_val = rem_val + (rem_val*(6.5/1200))
    if new_val < 0 and c < 1:
        months = m 
        c = c + 1
    else:
        monthly_val4.append(new_val)
        m = m + 1
print("Repayments in ", months//12, " years and ", months % 12, "months")

plt.xlim(0,60)
plt.ylim(0,100000) 
plt.xlabel("Number of months")   
plt.ylabel("Debt")
plt.plot(monthly_val1, label="1000")
plt.plot(monthly_val2, label="2000")
plt.plot(monthly_val3, label="3000")
plt.plot(monthly_val4, label="4000")
plt.legend()
plt.show()

print("Q3.c")
m = 1
c = 0
months = 0
num = int(input("Please enter monthly repayments: "))
rem_val = monthly_val5[m-1] - num
new_val = rem_val + (rem_val*(6.5/1200))
if num < rem_val*(6.5/1200):
    print("Debt will never be paid")
else:
    while m<1000:              #m is an arbitrary big number
        rem_val = monthly_val5[m-1] - num
        new_val = rem_val + (rem_val*(6.5/1200))
        if new_val < 0 and c < 1:
            months = m 
            c = c + 1
        else:
            monthly_val5.append(new_val)
            m = m + 1
    print("Repayments in ", months//12, " years and ", months % 12, "months")