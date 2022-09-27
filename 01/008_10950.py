import sys
sys.stdin = open("input.txt","r")
# 8. https://www.acmicpc.net/problem/10950 : A+B-3
T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    print(a+b)
    



