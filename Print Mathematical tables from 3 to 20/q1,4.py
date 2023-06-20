#num1 = int(input("Enter starting number: "))
#num2= int(input("Enter ending number: "))

f = open("inq1.txt","r")
#print(f.read())

num1,num2 = f.read().split(",")
#print(type(num1))
#num2,num3 = num1.split(",")
num1 = int(num1)
num2 = int(num2)
#print(type(num1))
#print(type(num2))
#num2 = int(f.read())

#print()
f1 = open("out.txt", "w")
for i in range(num1,num2+1):
    for j in range(1,11,1):
        f1.write("{0}*{1} ={2}".format(i,j,i*j))
        f1.write("\n")
    f1.write("\n")
f1.close()
