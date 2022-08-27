#!/usr/bin/env python
# coding: utf-8

# In[2]:


#no3
given = open('input3.txt','r')
received = open('output3.txt','w')
n = int(given.readline())
iD = given.readline().split()
mark = given.readline().split()
for a in range(n):
    mark[a] = int(mark[a])
def insert(iD,mark):
    for i in range(len(mark)-1):
        temp = mark[i+1]
        temp2 = iD[i+1]
        for j in range(i,-2,-1):
            if mark[j]>=temp:
                mark[j+1] = mark[j]
                iD[j+1] =iD[j]
            else:
                break
        mark[j+1] = temp
        iD[j+1] = temp2
        #print(mark)
    iD = iD[::-1]
    return iD
st = ''
final = insert(iD,mark)
for a in range(n):
    st = st+' '+str(final[a])
received.write(st)
given.close()
received.close()

#print(insert(myid,mymarks))

