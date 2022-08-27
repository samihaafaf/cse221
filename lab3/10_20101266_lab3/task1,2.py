#!/usr/bin/env python
# coding: utf-8

# In[1]:


#graph created and BFS implemented
from queue import Queue
my_queue = Queue()
given = open('lab3input.txt','r')
received = open('lab3output1.txt','w')
endnode  = int(given.readline())
bfs_graph = {}
for a in range(endnode):
    lis = given.readline().split()
    val = lis[1::]
    bfs_graph[lis[0]] = val
#print(bfs_dict)
visited = {}
for vertex in bfs_graph.keys():
    visited[vertex] = False

bfs_seq = []
def bfs(visited,graph,start,end):
    visited[start] = True
    my_queue.put(start)
    while not my_queue.empty():
        x = my_queue.get()
        #print('print x',x)
        #print(type(x))
        bfs_seq.append(x)
        if x==end:
            
            break
        else:
            for y in bfs_graph[x]:
                #print('x is',x,': y is',y)
                if visited[y]==False:  #not visited
                    visited[y] = True
                    my_queue.put(y)
            #print('\n')
    #print(bfs_seq)

        
bfs(visited,bfs_graph,'1','12')   
st = 'Places:'
for a in bfs_seq:
    st = st + ' '+a
received.write(st)    
given.close()    
received.close()


# In[ ]:




