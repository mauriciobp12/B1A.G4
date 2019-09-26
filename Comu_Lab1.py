#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Prueba de fucncionamiento

import numpy as np
import cmath
import math


# In[8]:


t=np.linspace(0,0.5,100);
x=int(input("ingrese un numero: "));
y=int(input("ingrese un numero: "));


# In[9]:


z=x+y;
f=np.cos(2*math.pi*t);
h=np.exp(2j*math.pi*t);


# In[6]:


print("La suma de kis nueros es: ",z)
print("funcion coseno: ",f)
print("funcion exponencial: ",h)


# In[ ]:




