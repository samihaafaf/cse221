#!/usr/bin/env python
# coding: utf-8

# In[2]:


#graph created and DFS implemented
given = open('lab3input.txt','r')
received = open('lab3output2.txt','w')
endnode  = int(given.readline())
dfs_graph = {}
for a in range(endnode):
    lis = given.readline().split()
    val = lis[1::]
    dfs_graph[lis[0]] = val

visited = {}
for vertex in dfs_graph.keys():
    visited[vertex] = False

dfs_seq = []
def dfsvisit(graph,node):
    visited[node] = True
    dfs_seq.append(node)
    for y in dfs_graph[node]:
        #print('x is',x,': y is',y)
        if visited[y]==False:  #not visited
            dfsvisit(graph,y)
def dfs(graph,end):
    f_seq = 'Places: '
    for node in dfs_graph.keys():
        
        if visited[node]== False:
            dfsvisit(graph,node)
    for a in dfs_seq:
        if a==end:
            f_seq = f_seq + ' '+a
            break
        else:
            f_seq = f_seq + ' '+a
    return f_seq
    

    
    #return dfs_seq
    #print('\n')
#print(bfs_seq)

        
dfsvisit(dfs_graph,'1')  
st = dfs(dfs_graph,'12')
received.write(st)    
given.close()    
received.close()


# In[ ]:




