#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#task1 ok
info = {'Y':'Yasnaya','P':'Pochinki','S':'School','R':'Rozhok','F':'Farm','M':'Mylta','H':'Shelter','I':'Prison'}
given = open('input1.txt','r')
received = open('output1.txt','w')
zones = int(given.readline())
s2 = given.readline().strip()
s1 = given.readline().strip()
def LCS(string1,string2):
    #string2 = string2[0:len(string2)-1]
    m = len(string1)+1
    n = len(string2)+1
    c = [[0]*(m) for i in range(n)]
    t = [[None]*(m) for i in range(n)]
    for i in range(1,m):
        for j in range(1,n):
            if string1[i-1]==string2[j-1]:
                c[i][j] = c[i-1][j-1]+1
                t[i][j] = 'diagonal'
            elif c[i-1][j]>=c[i][j-1]:
                c[i][j] = c[i-1][j]
                t[i][j] = 'up'
            else:
                c[i][j] = c[i][j-1]
                t[i][j] = 'left'
    a = m-1
    b = n-1
    store = []
    while a>=1 and b>=1:
        if t[a][b]=='diagonal':
            store.append(string2[b-1])
            a = a-1
            b = b-1
        elif t[a][b]=='up':
            a = a-1
        else:
            b = b-1
    store.reverse()
    return store,c[m-1][n-1]
things,cor = LCS(s1,s2)
places = ''
for i in range(len(things)):
    places = places+info[things[i]]+' '
cor = str((cor*100)//zones)
received.write(places+'\n'+ 'Correctness of prediction:' + cor+'%' )
#print(places,cor)
given.close()    
received.close()

