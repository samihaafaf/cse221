#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#task1 lab4

import queue

given = open('lab4input1.txt','r')
received = open('lab4task1.txt','w')
def dijkstra(graph,s,nodes):
    d = [0]*(nodes+1)
    parent = [0]*(nodes+1)
    for i in range(1,nodes+1):
        d[i] = 99999
        parent[i] = None
    d[s] = 0
    visited = []
    min_heap = queue.PriorityQueue()
    for i in range(1,nodes+1):
        min_heap.put((d[i],i))
    while not min_heap.empty():
        u = min_heap.get()[1]
        if u not in visited:
            visited.append(u)
            for v in graph[u]:
                if d[v]>d[u]+int(graph[u][v]) and v not in visited:
                    d[v] = int(d[u])+int(graph[u][v])
                    parent[v] = u
                    min_heap.put((d[v],v))
    return d[5]
test = int(given.readline())
op = []
for a in range(test):
    place_road = given.readline().split()
    for x in range(len(place_road)):
        place_road[x] = int(place_road[x])
    
    if place_road[1]==0:
        op.append(0)
    elif place_road[1]==1:
        path = given.readline().split()
        op.append(int(path[2]))
    else:
        dij_graph = {}
        #now make a graph from the lines
        for a in range(place_road[1]):  #making the graph
            
            lis = given.readline().split()
            place = int(lis[0])
            if place not in dij_graph.keys():
                inner_dict = {}
                inner_dict[int(lis[1])] = int(lis[2])
                dij_graph[place] = inner_dict
            else:
                dij_graph[place][int(lis[1])] = int(lis[2])
            if len(dij_graph)!= place_road[0]:
                for a in range(1,place_road[0]+1):
                    if a not in dij_graph.keys():
                        dij_graph[a] = {} 
                
        
        print(dij_graph)
        out = dijkstra(dij_graph,1,place_road[0])
        op.append(out)
        

                    
                
print(op)        
for a in range(len(op)):
    received.write(str(op[a]))
    received.write('\n')

given.close()    
received.close()    
        
        
            
        
    
   

