import re


def summ(a):
    summa = 0
    for i in range(len(a)):
        summa += a[i]
    return summa

def umnojit(a):
    out_um = 1
    for i in range(len(a)):
        out_um *= a[i]
    return out_um

in_a = [int(i) for i in input("Введи числа: ").split()]
choice = int(input("1 для умножить 2 для сложить: "))

if choice == 1:
    print(umnojit(in_a))
elif choice == 2:
    print(summ(in_a))
else:
    print("ERROR")