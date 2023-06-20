'''
DRY-word[0]+word[1]+word[2]
DYR-word[0]+word[2]+word[1]

RDY-word[1]+word[0]+word[2]
RYD-word[1]+word[2]+word[0]

YDR-word[2]+word[0]+word[1]
YRD-word[2]+word[1]+word[0]
'''
'''
SEAT-word[0]+word[1]+word[2]+word[3]
SETA-word[0]+word[1]+word[3]+WORD[2]
SAET-word[0]+word[2]+word[1]+WORD[3]
SATE-word[0]+word[2]+word[3]+WORD[1]
STEA-word[0]+word[3]+word[1]+WORD[2]
STAE-word[0]+word[3]+word[2]+WORD[1]
ESAT
ESTA
EAST
EATS
ETSA
ETAS

'''
word4="SEAT"
wordnew=[]
for i in range(len(word4)):
    wordnew.append(word4[i])
#print(wordnew)

#new1=word4[0]
#new2=word4[1]+word4[2]+word4[3]

def perm4(word3):
    word=word3
    list1=[]               
    for i in range(len(word)):
        word1=word[i]
        word[0],word[i]=word[i],word[0]
        print("1",word)
        #for j in range(1,len(word)):
        new=word1+word[1]+word[2]+word[3]
        list1.append(new)
        new=word1+word[1]+word[3]+word[2]
        list1.append(new)
        new=word1+word[2]+word[1]+word[3]
        list1.append(new)
        new=word1+word[2]+word[3]+word[1]
        list1.append(new)
        new=word1+word[3]+word[1]+word[2]
        list1.append(new)
        new=word1+word[3]+word[2]+word[1]
        list1.append(new)
    print(list1)
    print(len(list1))
perm4(wordnew)


