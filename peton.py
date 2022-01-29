import re


def summ(a):
    summa = 0
    for i in range(len(a)):
        summa += a[i]
    return summa

in_a = [int(i) for i in input().split()]
print(summ(in_a))