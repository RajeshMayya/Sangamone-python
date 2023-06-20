num1 = 3
num2= 20

for i in range(num1,num2+1):
    for j in range(1,11,1):
        print("{0}*{1} ={2}".format(i,j,i*j))
    print()
