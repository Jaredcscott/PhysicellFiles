from math import asin
import numpy as np
import matplotlib.patches as mpatches

ox = 0
oy = 0
points=50
offset=0.0
tau=(1+5**0.5)/2.0          # golden ratio approx = 1.618033989
inc = (2-tau)*2*np.pi + offset
theta=0
k=0.1 # scale factor
drad=k*(1+5**0.5)/4.0 # radius of each disc
minv=maxv=0 # minv and maxv will be used later to display inputs chosen

for j in range(1,points+1):
    r = k*j**0.5
    theta += inc
    x = ox + r*np.cos(theta)
    y = oy + r*np.sin(theta)
    if y > maxv:
        maxv=y
    elif y < minv:
        minv=y
    disc = mpatches.Circle((x,y),drad) 
    print(int(x * 450),",",int(y *450),",",0,",",3)

    
