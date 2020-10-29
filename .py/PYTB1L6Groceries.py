#!/usr/bin/env python
# coding: utf-8

# In[8]:


Boodschappelijst= ["brood", "melk", "pita"]
Winkelmand=["brood", "melk", "pita", "frisdrank"]

for x in Winkelmand:
    if x in Boodschappelijst:
        print(x + " Klaar")
    else: 
        print(x + " extra")

