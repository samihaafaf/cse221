#!/usr/bin/env python
# coding: utf-8

# In[3]:


#task4 
given = open('input4.txt','r')
received = open('output4.txt','w')
n = int(given.readline())
array = given.readline().split()
for a in range(n):
    array[a] = int(array[a])
def merge(ar1,ar2):
    i,j,k = 0,0,0
    aux = []
    while (i<len(ar1)) and (j<len(ar2)):
        if ar1[i]<ar2[j]:
            aux.append(ar1[i])
            #my[k] = ar1[i]
            i = i+1
        else:
            aux.append(ar2[j])
            #my[k] = ar2[j]
            j = j+1
        k = k+1
    while i<len(ar1):
        aux.append(ar1[i])
        #my[k] = ar1[i]
        i = i+1
    while j<len(ar2):
        #my[k] = ar2[j]
        aux.append(ar2[j])
        j = j+1
    #print('aux is',aux)
    return aux
def mergesort(my):
    if len(my)==1:
        return my
    else:
        mid = len(my)//2
        ar1 = my[:mid]
        ar2 = my[mid:]
        a = mergesort(ar1)
        #print('a is ',a)
        b = mergesort(ar2)
        #print('b is',b)
        return merge(a,b)
st = ''
sorted_ar = mergesort(array)
for a in range(n):
    st = st+' '+str(sorted_ar[a])
received.write(st)
given.close()
received.close()
#print(mergesort(myAr))
#print(myAr)


# In[ ]:




