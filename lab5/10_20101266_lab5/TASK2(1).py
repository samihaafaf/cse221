#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#task2
given = open('input2.txt','r')
received = open('output2.txt','w')
task,ppl = given.readline().split()
stor = []
for a in range(int(task)):
    start, stop = given.readline().split()
    val = [[],[]]
    val[0] = int(start)
    val[1] = int(stop)
    stor.append(val)
stor = sorted(stor, key=lambda stor:stor[1])
def work(info,men):
    count = 0
    for each in range(men):
        end_time = 0
        for a in info:
            if a[0]!=None and a[0]>=end_time:
                end_time = a[1]
                count+=1
                a[0]= None
                #print(info)
    return count
ans = str(work(stor,int(ppl)))
received.write(ans)
given.close()    
received.close() 

