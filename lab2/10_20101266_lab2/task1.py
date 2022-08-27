#!/usr/bin/env python
# coding: utf-8

# In[48]:


#task1
given = open('input1.txt','r')
received = open('output1.txt','w')
n = int(given.readline())
arr = given.readline().split()
#print(arr)
for a in range(n):
    arr[a] = int(arr[a])
#print(arr)
def bubble(ar):
    check = 0
    for a in range(len(ar)-1,1,-1):       #checks if the array is already sorted or not, this checking process takes
        if (ar[a])<(ar[a-1]):                  # n times comparing so the complexity is theta of n. A sorted array gives                               #best case for bubble sort.
            check = 1
            break
    if check==0:                       #if array is sorted just return the array without any further sorting.
        return ar
    else:
        for a in range(1,len(ar)):
            for b in range(a,0,-1):
                if (ar[b])<(ar[b-1]):
                    temp = ar[b]
                    ar[b] = ar[b-1]
                    ar[b-1] = temp
                #print('ar is',ar,'b is ',b,'a is',a)
    return ar
st = ''
#print(bubble(arr))
arr = bubble(arr)
for a in range(len(arr)):
    st = st+' '+str(arr[a])
received.write(st)
given.close()
received.close()

#The best case of a bubble algorithm is when it is already sorted.The first loop inside my bubble sort checks whether an array is already sorted or not, if it is sorted then with only after n operations the function returns the array without any further operations. So the time complexity for best case is theta of n.
                

