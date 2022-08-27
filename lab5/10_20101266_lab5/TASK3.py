#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#task3
given = open('input3.txt','r')
received = open('output3.txt','w')
chores = given.readline()
hrs=[int(each) for each in given.readline().split()]
hrs.sort()
seq = given.readline()
track = ''
Jack_done = []
ja,ji = 0,0
c = 0
for each in range(len(seq)):
    if seq[each]=='J':
        #print('hi jack')
        ja += hrs[c]
        track =  track + str(hrs[c])
        Jack_done.append(hrs[c])
        c+= 1
    else:
        #print('hi jill')
        x = Jack_done.pop()
        ji += x
        track = track + str(x)

received.write(track+'\n')
received.write('Jack will work for {} hours'.format(ja)+'\n'+'Jill will work for {} hours'.format(ji))
#print('track is',track)
#print(hrs)
#print(seq)
    
given.close()    
received.close()

