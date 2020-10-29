#!/usr/bin/env python
# coding: utf-8

# In[4]:



import sys
import time

def Kassa(begroete, betaling):
  print("&: Goedendag")
  time.sleep(1)
  print("&: Hoeft u alles gevonden?")
  time.sleep(1)
  print("#: " + begroete)
  time.sleep(1)
  print("&:" + "Hoe wilt u betalen, pinnen of contant")
  time.sleep(1)
  print("#: graag" + betaling )
  time.sleep(1)
  print("&: fijne dag nog")

Kassa(sys.argv[1], sys.argv[2])

