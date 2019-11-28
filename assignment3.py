#!/usr/bin/env python
# coding: utf-8

# In[5]:


a=int(input("enter the first number"))
b=int(input("enter the second number"))
operator=input("enter operator")

if operator == "+":
    ans =(a+b)
    print(ans)
    
elif operator == "-":
    ans1 =(a-b)
    print(ans1)

elif operator == "*":
    ans2 =(a*b)
    print(ans2)
    
elif operator == "/":
    ans3 =(a/b)
    print(ans3)
    
elif operator == "**":
    ans4 =(a**b)
    print(ans4)
    
else:
    print("you select wroung operator:")


# In[ ]:





# In[6]:


d = {0:10, 1:20}  
print(d)  
d.update({2:30})  
print(d)  


# In[7]:


def returnSum(myDict): 
      
    sum = 0
    for i in myDict: 
        sum = sum + myDict[i] 
      
    return sum
  
# Driver Function 
dict = {'a': 100, 'b':200, 'c':300} 
print("Sum :", returnSum(dict)) 


# In[8]:


def unique_list(list):
    uniq_list =[]
    uniq_set = set()
    for item in list:
        if item not in uniq_set:
            uniq_list.append(item)
            uniq_set.add(item)
    return uniq_list
list = [10,20,30,10,10,30,40,50]
print(unique_list(list))


# In[ ]:


d={1:10,2:20,3:30,4:40,5:50,6:60}
def is_key_present(x):
    if x in d:
        print('key is present in the dictionary')
    else:
        print('key is not present in the dictionary')
is_key_present(5)
is_key_present(9)

