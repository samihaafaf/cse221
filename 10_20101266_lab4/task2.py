#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#tassk2 lab4

import queue

given = open('lab4input1.txt','r')
received = open('lab4task2.txt','w')
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
    
    def p(node,source):
        path = []
        while node!=source:
            path.append(str(node))
            node = parent[node]
        path.append(str(node))
        path.reverse()
        return path
    pathmain = p(nodes,s)
        
    return pathmain
test = int(given.readline())
op = []
path = []
for a in range(test):
    place_road = given.readline().split()
    for x in range(len(place_road)):
        place_road[x] = int(place_road[x])
    
    if place_road[1]==0:
        op.append(0)
        path.append(list(str(1)))
    elif place_road[1]==1:
        lis = given.readline().split()
        path.append([])
        path[len(path)-1].append(lis[0])
        path[len(path)-1].append(lis[1])
        
    else:
        dij_graph = {}
        for a in range(place_road[1]):  
            
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
        
                
        
        path.append(dijkstra(dij_graph,1,place_road[0]))
#print(path)
for x in path:
    for y in x:
        #print('y is',y)
        received.write(y)
    received.write('\n')
        
       
given.close()    
received.close()    
           

