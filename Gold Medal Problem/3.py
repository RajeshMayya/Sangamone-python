names = []
subjects=[]
sub1 = []
sub2=[]
sub3=[]
sub4=[]
sub5 = []
toppers_sub1=[]
toppers_sub2=[]

f1 = open('marks.txt','r')
context = f1.readlines()
lenline = len(context)
#print(lenline)

for i in range(0,lenline):
    list1 = context[i].split(',')
    #print(list1[0])
    names.append(list1[0])
    
    list2 = list1[3].split(':')
    subjects.append(list2[0])
    sub1.append(int(list2[1]))
    #print(list2[1])

    list2= list1[4].split(':')
    subjects.append(list2[0])
    sub2.append(int(list2[1]))

    list2 = list1[5].split(':')
    subjects.append(list2[0])
    sub3.append(list2[1])

    list2 = list1[6].split(':')
    subjects.append(list2[0])
    sub4.append(list2[1])

    list2 = list1[7].split(':')
    subjects.append(list2[0])
    sub5.append(list2[1])

maxsub1=max(sub1)
maxsub2=max(sub2)
maxsub3=max(sub3)
maxsub4=max(sub4)
maxsub5=max(sub5)

for i in range(0,len(sub1)):
    if (sub1[i] == maxsub1):
        toppers_sub1.append(names[i])
    if(sub2[i] == maxsub2):
        toppers_sub2.append(names[i])
    print()

print(toppers_sub1,subjects[0],maxsub1)
print(toppers_sub2,subjects[1],maxsub2)
'''
82,72,84
82,84
84

95,98

95,98,100
'''
