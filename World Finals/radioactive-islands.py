# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2016 World Finals - Problem E. Radioactive Islands
# https://code.google.com/codejam/contest/7234486/dashboard#s=p4
#
# Time:  O(P^2*G^2), P is the granularity parameter of y, G is the number of grids
# Space: O(P*G)
#

# referenced from https://code.google.com/codejam/contest/scoreboard/do?cmd=GetSourceCode&contest=7234486&problem=5760632301289472&io_set_id=1&username=Gennady.Korotkevich

from sys import float_info
from math import sqrt

def D(C, x):
    dose = 0.0
    for c in C:
        dist = x[0]**2 + (x[1]-c)**2
        if dist < float_info.epsilon:
            return float("inf")
        dose += 1.0/dist
    return dose

def calc(C, a, b):
    a = (X_START + a[0]*X_STEP, Y_START + a[1]*Y_STEP)
    b = (X_START + b[0]*X_STEP,  Y_START + b[1]*Y_STEP)
    return (1.0+(D(C, a)+D(C, b))/2) * sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def radioactive_islands():
    N, A, B = map(float, raw_input().strip().split())
    C = map(float, raw_input().strip().split())
    dp = [float("inf")]*(Y_NUM+1)
    start_y = int((A-Y_START)/Y_STEP + 0.5)
    dp[start_y] = 0.0
    for i in xrange(1, X_NUM+1):
        new_dp = [float("inf")]*(Y_NUM+1)
        for j in xrange(Y_NUM+1):
            for k in xrange(max(0, j-K_NUM), min(Y_NUM, j+K_NUM)+1):
                new_dp[j] = min(new_dp[j], dp[k] + calc(C, (i-1, j), (i, k)))
        dp = new_dp
    finish_y = int((B-Y_START)/Y_STEP + 0.5)
    return dp[finish_y]

GRANULARITY = 11  # tuned by experiment
GRID_NUM = 50  # tuned by experiment
MAX_ABS_SLOPE = 2  # verified by experiment
X_START, X_END = -10.0, 10.0
Y_START, Y_END = -10.0, 10.0
X_NUM, Y_NUM = GRID_NUM, GRANULARITY*GRID_NUM
K_NUM = MAX_ABS_SLOPE*Y_NUM//X_NUM
X_STEP = (X_END-X_START)/X_NUM
Y_STEP = (Y_END-Y_START)/Y_NUM
for case in xrange(input()):
    print "Case #%d: %s" % (case+1, radioactive_islands())