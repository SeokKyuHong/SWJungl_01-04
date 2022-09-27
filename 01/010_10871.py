import sys
sys.stdin = open("input.txt","r")
# 10. https://www.acmicpc.net/problem/10871 : X보다 작은 수 

N, X = map(int, input().split())
A = list(map(int, input().split()))
for i in range(N):
    if X > A[i]:
        print(A[i])
