# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 17:05:38 2020

@author: giha
"""

import numpy as np
from loader import DataLoad
from bar import Bar, Bars
from edgeCal import EdgeCal
from psd import CalNClip, MovingAvg, PSD_hist, FOM_plot,PSD_ergslice
from timeHist import TimeHist
import matplotlib.pyplot as plt

plt.close('all')
lower = 35
upper = 64
'''
data = []


for i in range(upper - lower + 1):
    cache =  DataLoad('D:\X' + str(lower+i)  + 'data.p' )
    data.append(   cache    )

'''
def lin_interp(x, y, i, half):
    return x[i] + (x[i+1] - x[i]) * ((half - y[i]) / (y[i+1] - y[i]))

def FWHM(x, hist):
    half = np.max(hist)/2.0
    signs = np.sign(np.add(hist, -half))
    zero_crossings = (signs[0:-2] != signs[1:-1])
    zero_crossings_i = np.where(zero_crossings)[0]
    left = lin_interp(x, hist, zero_crossings_i[0], half)
    right = lin_interp(x, hist, zero_crossings_i[1], half)
    return right - left

pos0 = Bars(data[1])
pos1 = Bars(data[3])
pos2 = Bars(data[6])
pos3 = Bars(data[8])
pos4 = Bars(data[11])
pos5 = Bars(data[14])
pos6 = Bars(data[17])
pos7 = Bars(data[20])
#pos8 = Bars(data[23])
pos9 = Bars(data[25])
pos10 = Bars(data[28])



allpos = [pos0, pos1, pos2, pos3, pos4, pos5, pos6, pos7,  pos9, pos10]
pos = [0, 5, 10, 15, 20, 25, 30, 35,  45, 50]
binedges = np.linspace(0,1,301)
center = (binedges[:-1] + binedges[1:]) / 2
maxes = []
FWHMs = []

plt.figure()
for j in range(len(allpos)):
    # plt.hist(allpos[j][2][6], bins=500, density = True, label = str(j*5)+ 'mm' , alpha = 0.5 )    
    hist = plt.hist(allpos[j][0][6], bins=binedges, density = True, label = str(pos[j])+ 'mm' , alpha = 0.7 ) 
    maxes.append(   center[np.argmax(hist[0])] )
    FWHMs.append(FWHM(center, hist[0])   )
    
    
    
plt.xlabel('Bottom/Total')
plt.xlim((0,1))
plt.legend()
plt.tight_layout()



plt.figure()
plt.errorbar(pos, maxes, yerr=np.array(FWHMs)/2.355, ls='none', marker = '.',elinewidth=1, capsize=5)

p = np.polyfit(pos, maxes, 3)
x = np.linspace(0,50,1001)
plt.plot(x, p[0]*x**3 + p[1]*x**2 + p[2]*x + p[3] )


plt.xlabel('Height (mm)')
plt.ylabel('Bottom/Total')
plt.xlim((-5,55))
plt.tight_layout()


