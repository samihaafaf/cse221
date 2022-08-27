#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#test4
import math
import queue
given = open('lab4input2.txt','r')
received = open('lab4task2.txt','w')

def network(graph,source):
    #print('graph is',graph)
    d = [0]*(len(graph)+1)
    parent = [0]*(len(graph)+1)
    d[int(source)] = math.inf
    visited = []
    max_heap = queue.PriorityQueue()
    for i in range(1,len(graph)+1):
        if i!=source:
            d[i] = -math.inf
        parent[i] = None
        max_heap.put((d[i]*(-1),i))
    #print('helo')
    while not max_heap.empty():
        u = max_heap.get()[1]
        #print('u is',u)
        #extract max from max_heap
        #if u not in visited:
            #visited.append(u)
        for v in graph[u]:
            alt = min(d[u],graph[u][v])
            if alt>d[v]:
                d[v] = alt
                parent[v] = u
                max_heap.put((d[v]*(-1),v))
    #print('end met')
    for i in range(1,len(d)):
        if d[i]==math.inf:
            d[i] = 0
        if d[i]==-math.inf:
            d[i] = -1
    d = d[1::]
    return d

        
test = int(given.readline())
#print('test is',test)
for a in range(test):
    #print('test going on:',a)
    x,y = given.readline().split()
    if int(y)==0:
        source = given.readline()
        for x in range(int(x)):
            received.write(' ')
            received.write(str(0))
        received.write('\n')
        
        
    else:
        dic = {}
        for b in range(int(y)):
            u,v,weight = given.readline().split()
            u = int(u)
            v = int(v)
            weight = int(weight)
            if u not in dic.keys():
                inner_dict = {}
                inner_dict[v] = weight
                dic[u] = inner_dict
            else:
                dic[u][v] = weight
        #print('u is',u)
        #print('dic leng',len(dic))
        if len(dic)!= x:
            for a in range(1,int(x)+1):
                if a not in dic.keys():
                    dic[a] = {}
        #print('graph created is ',dic)
        s = given.readline()
        lis = network(dic,int(s))
        st = ''
        for a in range(len(lis)):
            st = st+' '+str(lis[a])
        received.write(st)
        received.write('\n')
    


given.close()    
received.close()    
           

