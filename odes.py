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
    
    for i in range(1, len(uk)):
        uk[i] = uk[i-1] + dt*u2k[i-1]
        u2k[i] = u2k[i-1] - dt*uk[i-1]    
    