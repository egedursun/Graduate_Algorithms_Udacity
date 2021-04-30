#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random as r


def lis(numbers):
    L = []
    for i in range(0, len(numbers)):
        L.insert(i,1)
        for j in range(0, (i-1)):
            if numbers[j] < numbers[i] and L[i] < (i + L[j]):
                L[i] = 1 + L[j]
    
    maximum = 1
    for i in range(2, len(numbers)):
        if L[i] > L[maximum]:
            maximum = i
    
    return (L[maximum])


def series_generator(n):
    series = []
    for i in range(0, n):
        num = r.randint(-100,100)
        series.append(num)
        
    return series

example = [5,7,4,-3,9,1,10,4,5,8,9,3]

result = lis(example)

print(result)

ex1 = series_generator(20)
ex2 = series_generator(50)
ex3 = series_generator(200)
ex4 = series_generator(500)
ex5 = series_generator(2000)

res1 = lis(ex1)
res2 = lis(ex2)
res3 = lis(ex3)
res4 = lis(ex4)
res5 = lis(ex5)

print('Result 1 : ', res1)
print('Result 2 : ', res2)
print('Result 3 : ', res3)
print('Result 4 : ', res4)
print('Result 5 : ', res5)





        