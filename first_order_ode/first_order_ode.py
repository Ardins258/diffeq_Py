# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 02:25:40 2021

@author: Aerial
"""
#lib import
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#define FIRST ORDER ODE function
def fo(y,t):
    zeta = 5
    K = 2
    u = 1
    dydt = (-y + K*u)/zeta
    return dydt

# Integrate the defined function
# If you are solving for y(t) then you will have to use the name of your function in the first paranthesis and then the points (t) that you wanna solve for
# odeint for "fo" at starting time zero and 5 points 
y = odeint(fo,0,[1,2,3,4,5,6,7,8,9,10])
print(y)

# those very 5 points could as well be put into one t function using numpy and then place the t instead of points in odeint.
t = np.linspace(0,10,11)
print(t)
y2 = odeint(fo,0,t)
print(y2)

# As you can see the answers for y and y2 will be the same 
# We will be plotting the ode answer and since y1 and y2 are the same it doesn't matter which one we plot for, just gonna use y2
plt.figure()
plt.plot(t,y2,color='red',label="Ans for $[dy/dt=(-y+ku)/\zeta ]$")
#gonna plot y+1 so it can be seen on the plot data and and two don't overwrite each other
plt.plot(y+0.1,color='blue',label="Ans for $[dy/dt=(-y+ku)/\zeta ]+0.1$")
plt.legend()
plt.show()
