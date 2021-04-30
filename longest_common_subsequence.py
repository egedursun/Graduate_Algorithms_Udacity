#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def lcs(x, y):
    
    n = min([len(x),len(y)])
    
    L = [[0 for i in range(n+1)] for j in range(n+1)] 
    
    for i in range(0, n+1):
        L[i][0] = 0
    
    for j in range(0, n+1):
        L[0][j] = 0
    
    for i in range(0, n+1):
        for j in range(1, n+1):
            if x[i] == y[j]:
                L[i][j] = (1 + L[i-1][j-1])
                print(i, ' and ', j, ' is: ', L[i][j])
                
            else:
                L[i][j] = max((L[i][j-1],L[i-1][j]))
                print(i, ' and ', j, ' is: ', L[i][j])
    
    return L[n][n]


x = ['B', 'C', 'D', 'B', 'C', 'D', 'A']
y = ['A', 'B', 'E', 'C', 'B', 'A']

result = lcs(x, y)

print(result)

