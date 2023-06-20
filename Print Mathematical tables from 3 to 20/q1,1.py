num1 = int(input("Enter starting number: "))
num2= int(input("Enter ending number: "))
print()
for i in range(num1,num2+1):
    for j in range(1,11,1):
        print("{0}*{1} ={2}".format(i,j,i*j))
    print()
