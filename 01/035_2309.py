import sys
from itertools import combinations
sys.stdin = open("input.txt","r")
# 35.https://www.acmicpc.net/problem/2309 :일곱 난쟁이
input=sys.stdin.readline

N = [int(input()) for _ in range(9)]
n = []

result=list(combinations(N,7))


for i in range(len(result)):
    if sum(result[i]) == 100:
        Y = result[i]
        U = sorted(Y)
        for j in range(len(U)):
            print(U[j])
        break

