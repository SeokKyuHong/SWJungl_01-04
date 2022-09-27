import sys
sys.stdin = open("input.txt","r")
# 32. https://www.acmicpc.net/problem/2751 :수 정렬하기2
N = int(sys.stdin.readline())
N_list = [int(sys.stdin.readline()) for _ in range(N)]
N_list.sort()
for i in N_list:
    print(i)