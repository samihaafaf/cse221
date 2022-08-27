#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1
num = open('input.txt','r')
num2 = open('output.txt','w')
num3 = open('record.txt','w')
def pal(n = None):
    if n is None:
        return 'not a palindrome'
    else:
        nn = n[::-1]
        if n==nn:
            return 'is a palindrome'
        else:
            return 'not a palindrome'
i = 0
final = []
pal = 0
even = 0
odd = 0
nopar = 0
for i in range(5):     #storing in an array  taking input for 5 inputs
    test = [-1,-1]
    n = num.readline().split()
    if n[0].find('.')!=-1:   #decimal check
        nopar+=1
        test[0] = 'cannot have parity'
    elif int(n[0])%2==0:
        even+=1
        test[0] = 'is even'
    else:
        odd+=1
        test[0] = 'is odd'
    name = n[1]
    if name is None:
        test[1]= 'not a palindrome'
        
    else:
        nn = name[::-1]
        if name==nn:
            test[1] =  'is a palindrome'
            pal+=1
        else:
            test[1] =  'not a palindrome'
    #palresult = pal(name)
    #test[1] = palresult
    st = n[0]+' '+ test[0]+' and '+n[1]+' '+test[1]
    num2.write(st)
    num2.write('\n')
oddper = int((odd/5)*100)
num3.write('Percentage of odd parity: '+str(oddper)+' %')
num3.write('\n')
evenpar = int((even/5)*100)
num3.write('Percentage of even parity: '+str(evenpar)+' %')
num3.write('\n')
nopar = int((nopar/5)*100)
num3.write('Percentage of no parity: '+str(nopar)+' %')
num3.write('\n')
palper = int((pal/5)*100)
num3.write('Percentage of palindrome: '+str(palper)+' %')
num3.write('\n')
nopal = int(((5-pal)/5)*100)
num3.write('Percentage non-palindrome: '+str(nopal)+' %')

num.close()
num2.close()
num3.close()

