#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#task1
given = open('input1.txt','r')
received = open('output1.txt','w')
n = int(given.readline())
main = []
for a in range(n):
    start, stop = given.readline().split()
    tup = (int(start),int(stop))
    main.append(tup)
main = sorted(main, key=lambda main:main[1])
def assi_selection(main,n):
    selected = []
    end_time = 0
    for assi in main:
        if assi[0]>=end_time:
            end_time = assi[1]
            selected.append(assi)
    return selected
todo_assi = assi_selection(main,n)  
received.write(str(len(todo_assi)))  #count is the len of the selected array
received.write('\n')
for a in todo_assi:
    op = str(a[0])+' '+str(a[1])
    received.write(op)
    received.write('\n')

given.close()    
received.close()    
        

