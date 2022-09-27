import sys
sys.stdin = open("input.txt","r")
# 31. https://www.acmicpc.net/problem/2750 :수 정렬하기
N = int(input())
N_list = [int(input()) for _ in range(N)]
N_list.sort()
for i in N_list:
    print(i)