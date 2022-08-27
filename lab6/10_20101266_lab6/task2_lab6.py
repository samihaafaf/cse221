#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#task 2 ok
given=open('input2.txt')
s1=given.readline().strip()
s2=given.readline().strip()
s3=given.readline()
received=open('output2.txt','w')

def LCS(s1,s2,s3):
    m=len(s1)+1
    n=len(s2)+1
    o=len(s3)+1
    c = [[[0]*(o) for i in range(n)] for j in range(m)]
    t = [[[None]*(o) for i in range(n)] for j in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            for k in range(1,o):
                if s1[i-1]==s2[j-1] and s1[i-1] == s3[k-1]:
                    c[i][j][k]=1+c[i-1][j-1][k-1]
                    t[i][j][k]='diagonal'
                else:
                    if c[i-1][j][k]>=c[i][j-1][k]:
                        maxi=c[i-1][j][k]
                        if maxi>=c[i][j][k-1]:
                            c[i][j][k]=maxi
                            t[i][j][k]='up-up-left'
                        else:
                            maxi =c[i][j][k-1]
                            c[i][j][k]=maxi
                            t[i][j][k]='left-up-up'
                    else:
                        maxi =c[i][j-1][k]
                        if maxi>=c[i][j][k-1]:
                            c[i][j][k]=maxi
                            t[i][j][k]='up-left-up'
                        else:
                            maxi=c[i][j][k-1]
                            c[i][j][k]=maxi
                            t[i][j][k]='left-up-up'
    #print(c)
    return c[m-1][n-1][o-1]
val=str(LCS(s1,s2,s3))
#print(val)
received.write(val)
received.close()

