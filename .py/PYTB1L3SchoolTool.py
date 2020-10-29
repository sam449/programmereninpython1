#!/usr/bin/env python
# coding: utf-8

# In[85]:


weekdag=("maandag", "dinsdag", "woensdag", "donderdag", "vrijdag")
vrijedagen=("zaterdag", "zondag")
A=["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag"]
B=["zaterdag", "zondag"]


# In[86]:


def antwoordA():
    print('Schooldag')


# In[87]:


def antwoordB():
    print('Vrijedag')


# In[88]:


def dagen(): #functie
   print("Op welke dagen ben jij vrij van school?")
   A=["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag"]
   B=["zaterdag", "zondag"]
   print( A + B)
   antwoordD = input()
   if antwoordD in A:          
       antwoordA()
   elif antwoordD in B:
       antwoordB()


# In[89]:


dagen()


# In[ ]:





# In[ ]:




