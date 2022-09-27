import sys
from tkinter import W
sys.stdin = open("input.txt","r")
# # 22.https://www.acmicpc.net/problem/9020 : 골드바흐의 추축
def Goldbach():
    check = [False, False] + [True] * 10000    
    for i in range(2, 101):
        if check[i] == True:
            for j in range(i + i, 10001, i):
                check[j] = False

    T = int(input())
    for _ in range(T):
        n = int(input())

        A = n // 2
        B = A
        for _ in range(10000):
            if check[A] and check[B]:
                print(A, B)
                break
            A -= 1
            B += 1

Goldbach()





# a+b를 더해서 n 이 나오는 a, b가 있고,
# 이 a, b는 무조건 소수이면서 a-b가 제일 작은 수 
# a, b 를 구하시오 
