'''
DRY-word[0]+word[1]+word[2]
DYR-word[0]+word[2]+word[1]

RDY-word[1]+word[0]+word[2]
RYD-word[1]+word[2]+word[0]

YDR-word[2]+word[0]+word[1]
YRD-word[2]+word[1]+word[0]
'''
word="SEAT"
new1=word[0]
new2=word[1]+word[2]+word[3]
def perm3(word3):
    
    word=word3
    list1=[]
    new=word[0]+word[1]+word[2]
    list1.append(new)
    new=word[0]+word[2]+word[1]
    list1.append(new)
    new=word[1]+word[0]+word[2]
    list1.append(new)
    new=word[1]+word[2]+word[0]
    list1.append(new)
    new=word[2]+word[0]+word[1]
    list1.append(new)
    new=word[2]+word[1]+word[0]
    list1.append(new)
    print(list1)
perm3(new2)
