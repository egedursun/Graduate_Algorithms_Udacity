#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fib(n):
    F = []
    F.insert(0, 0)
    F.insert(1, 1)
    for i in range(2, n+1):
        F.insert(i, (F[i-1]+F[i-2]))
    return (F[n])


result = fib(7)
print(result)