import sys
sys.stdin = open("input.txt","r")
# 33.https://www.acmicpc.net/problem/10989 :수 정렬하기3
input= sys.stdin.readline

l = [0]*10000
print(l)
n = int(input())
for i in range(n):
    e=int(input())
    l[e-1] += 1
# print(l[0:10])

for i in range(len(l)):
    if l[i] != 0:
        for j in range(l[i]):
            print(i+1)
       
       