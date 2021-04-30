#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def lcs(x):
    S = []
    S.insert(0, 0)
    for i in range(0, len(x)):
        S.insert(i, (x[i] + max(0, S[i-1])))
    
    print('S: ', S)
    return max(S)


result = lcs([1,2,3,-5,8,-12,5,7,8,-4])
print('Result: ', result)