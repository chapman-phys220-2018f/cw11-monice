#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

###
# Name: Abby Wheaton, Monica Hiemer, and Royal Cuevas
# Student ID: 2299246
# Email: wheaton@chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2018
# Assignment: CW11
###


def euler(N, f0, f, t0=0, t=5*2*np.pi):
    
    n = np.linspace(t0, t, N)
    uk = np.zeros(N)
    u2k = np.zeros(N)
    dt = (t-t0)/N
    uk[0] = f0
    u2k[0] = f
    
    for i in range(1, len(uk)):
        uk[i] = uk[i-1] + dt*u2k[i-1]
        u2k[i] = u2k[i-1] - dt*uk[i-1]

        
    plt.plot(n, uk)
    plt.plot(n, u2k)
    
def heun(N, f0, f, t0=0, t=5*2*np.pi):
    
    n = np.linspace(t0, t, N)
    uk = np.zeros(N)
    u2k = np.zeros(N)
    dt = (t-t0)/N
    uk[0] = f0
    u2k[0] = f

    for i in range(1, len(n)):
        ubar = uk[i-1] + dt*u2k[i-1]
        upbar = u2k[i-1] - dt*uk[i-1]
        uk[i] = uk[i-1] + (dt/2)*(u2k[i-1] + upbar)
        u2k[i] = u2k[i-1] - (dt/2)*(ubar + uk[i-1])
       
        

    plt.plot(n, uk)
    plt.plot(n, u2k)

def kutta2(N, f0, f, t0=0, t=5*2*np.pi):
    n = np.linspace(t0, t, N)
    uk = np.zeros(N)
    u2k = np.zeros(N)
    dt = (t-t0)/N
    uk[0] = f0
    u2k[0] = f
    x1 = 0
    x2 =0
    y1=0
    y2=0
    
    for i in range(1, len(uk)):   
        x1 = dt*u2k[i-1]
        x2 = dt*(u2k[i-1]+x1/2)
        y1 = -dt*uk[i-1]
        y2 = -dt*(uk[i-1] + y1/2)
        uk[i] = uk[i-1] + x2
        u2k[i] = u2k[i-1] + y2
    plt.plot(n, uk)
    plt.plot(n, u2k)
    
def Kutta4(N, f0, f, t0=0, t=5*2*np.pi):
    n = np.linspace(t0, t, N)
    uk = np.zeros(N)
    u2k = np.zeros(N)
    dt = (t-t0)/N
    uk[0] = f0
    u2k[0] = f
    x1=0
    x2=0
    x3=0
    x4=0
    y1=0
    y2=0
    y3=0
    y4=0
    
    for i in range(1, len(uk)): 
        x1 = dt*u2k[i-1]
        x2 = dt*(u2k[i-1]+x1/2)
        x3 = dt*(u2k[i-1]+x2/2)
        x4 = dt*(u2k[i-1]+x3)
        uk[i] = uk[i-1]+(x1+2*x2+2*x3+x4)/6
        y1 = -dt*uk[i-1]
        y2 = -dt*(uk[i-1]+y1/2)
        y3 = -dt*(uk[i-1]+y2/2)
        y4 = -dt*(uk[i-1]+y3/3)
        u2k[i] = u2k[i-1]+(y1+2*y2+2*y3+y4)/6
        
    plt.plot(n, uk)
    plt.plot(n, u2k)
    
    
