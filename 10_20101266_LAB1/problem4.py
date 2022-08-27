#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#4
mmatA = open('inputA','r')
mmatB = open('inputB','r')
amr = open('multi','w')
n = int(mmatA.readline())
c = []    #initializing matricx C
for a in range(n):   #row of C
    st = []
    for b in range(n):    #colomns of C
        st.append(0)
    c.append(st)
matA = []
matB = []
for a in range(n):  #taking inout for matrix A
    stA = []
    stB = []
    for b in range(n):
        x = mmatA.readline()
        stA.append(x)
        x = mmatB.readline()
        stB.append(x)
    matA.append(stA)
    matB.append(stB)
for i in range(n):
    for j in range(n):
        for k in range(n):
            c[i][j]+=int(matA[i][k])*int(matB[k][j])
for i in range(n):
    for j in range(n):
        d = str(c[i][j])
        amr.write(d+',')
    amr.write('\n')
mmatA.close()
mmatB.close()
amr.close()

#print(mat)
#print(matA)
#print(matB)
#print(c)
        

