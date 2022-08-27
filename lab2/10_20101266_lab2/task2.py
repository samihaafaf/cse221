#!/usr/bin/env python
# coding: utf-8

# In[5]:


#task2
given = open('input2.txt','r')
received = open('output2.txt','w')
ar1 = given.readline().split()
price = given.readline().split()
#myar = [10,2,3,4,1,100,1]
for a in range(len(ar1)):
    ar1[a] = int(ar1[a])
for a in range(ar1[0]):
    price[a] = int(price[a])
def selsort(ar,m):
    counter = 0
    for a in range(len(ar)):
        if counter==m:
            break
        else:
            minval = ar[a]
            minindex = a
            for b in range(a,len(ar)):
                if ar[b]<minval:
                    minval = ar[b]
                    minindex = b
            temp = ar[a]
            ar[a] = minval
            counter+=1
            ar[minindex] = temp
    return ar[:m]
price = selsort(price,ar1[1])
st = ''
for a in range(len(price)):
    st = st+' '+str(price[a])
received.write(st)
given.close()
received.close()

#print(selsort(myar,4))


# In[ ]:




