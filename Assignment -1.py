#!/usr/bin/env python
# coding: utf-8

# 1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line. 

# In[1]:


for i in range(2000,3201):
    if i%5!=0 and i%7==0:
        print(i,end="")
        print(",",end="")


# 2. Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name

# In[2]:


first_name=input("Enter the first name :")
last_name=input("Enter the last name")
print(first_name[::-1],last_name[::-1])


# 3.Write a Python program to find the volume of a sphere with diameter 12 cm.  
#  
# Formula: V=4/3 * π * r 3 

# In[2]:


r=12/2
print("Volumne of a sphere is ",4/3*3.14*r)


# 4.Write a program which accepts a sequence of comma-separated numbers from console and generate a list. 

# In[32]:


n=input("Enter the no :")
x=n.split(",")
print(x)

5. Create the below pattern using nested for loop in Python. 
 
 
*  
* *  
* * * 
* * * *  
* * * * *  
* * * *  
* * *  
* *  
* 
 
 
# In[27]:


for i in range (0, 5):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")
#--------------------------------------
for i in range (5, 0, -1):
    for j in range(0, i -1):
        print("*",end=' ')
    print("\r")


## 6. Write a Python program to reverse a word after accepting the input from the user. 
 
Sample Output: 
 
Input word: iNeuron 
 
Output: norueNi
# In[1]:


x=input("Enter the name :")
print(x[::-1])


# 7. Write a Python Program to print the given string in the format specified in the ​sample output. 
#  WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all its citizens 
#  
# Sample Output: 
#  
# WE, THE PEOPLE OF INDIA,   having solemnly resolved to constitute India into a SOVEREIGN, !  SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC    and to secure to all its citizens 

# In[5]:


print("WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all its citizens")


# Note : - NOTE:​ ​The​ ​solution​ ​shared​ ​through​ ​Github​ ​should​ ​contain​ ​the​ ​source code​ ​used​ ​ and​  ​the​ ​output

# In[ ]:




