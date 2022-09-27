from itertools import count
import sys
sys.stdin = open("input.txt","r")
# 13.https://www.acmicpc.net/problem/4344 : 평균은 넘겠지
C = int(input())
N = [list(map(int, input().split())) for _ in range(C)]
for i in range(0,C):
    W = (sum(N[i])- N[i][0])/ N[i][0]
    count1=0
    for j in range(1,len(N[i])):
        if W < N[i][j]:
            count1 += 1        
    a = round((count1/(len(N[i])-1))*100,3)
    print(f"{a:.3f}%")

            



