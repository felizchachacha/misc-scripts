#!/usr/bin/env python2.7

import random

N=10

def hit(x,y):
    return y == 7 and 4 <= x <= 6

def get_ship(N):
    #result = []
    #for x in range(N):
    #    for y in range(N):
    #        if hit(x,y):
    #            result.append((x, y))
    #return result
    return [(x, y) for x in range(N) for y in range (N) if hit(x,y)]

print get_ship(N)

