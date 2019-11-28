#!/usr/bin/env python
# coding: utf-8

# In[37]:


#                                             ASSIGNMENT NO 2:
#                                            ------------------


#                                    1) Generate MARK SHEET Program:
#                                    -------------------------------
# Coding
math=int(input("enter the marks of math : "))
urdu=int(input("enter the marks of urdu : "))
eng=int(input("enter the marks of english : "))
m
isl=int(input("enter the marks of islamiate : "))
phy=int(input("enter the marks of physic : "))
tot=math+urdu+eng+isl+phy
tot=str(tot)
print("total obtain marks" + tot)
tot=int(tot)
per=((tot/500)*100)
print("per is {0:.3f}".format(per))
if per>=80:
    print("Your Grade Is : A+")
elif per>=70 and per<80:
    print("Your Grade Is : A")
elif per>=60 and per<70:
    print("Your Grade Is : B")
elif per>=50 and per<60:
    print("Your Grade Is : C")
else:
    print("Fail")

#OUTPUT:


# In[3]:


#                                    2) Identifier even or odd number:
#                                    -------------------------------
# Coding:
number=int(input("enter the number even or odd"))
if number%2==0:
    print("even number")
else:
    print("odd number")
#output:


# In[35]:


#                                    3) Print the length of the list:
#                                    -------------------------------
# Coding:
a=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55,89]
print("length of the list is :", len(a))
#output:


# In[36]:


#                                    4) sum the all numeric values in the list:
#                                    -----------------------------------------
# Coding:
a=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55,89]
b=a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]+a[8]+a[9]+a[10]
print("Sum of the list is ", b)
#Output:


# In[37]:


#                                    5) sum the all numeric values in the list:
#                                    -----------------------------------------
# Coding:
a=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55,89]
a.sort()
print("Largest number is", a[-1])


# In[1]:


#                                    6) sum the all numeric values in the list:
#                                    -----------------------------------------
# Coding:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in a:

    if i < 5:

        print(i)


# In[ ]:




