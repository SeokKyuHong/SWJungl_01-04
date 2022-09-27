import sys
sys.stdin = open("input.txt","r")
# 14.https://www.acmicpc.net/problem/2577: 숫자의 개수
A = [int(input()) for _ in range(3)]

gob = A[0]*A[1]*A[2]
N = list(map(int, str(gob)))
print(N)

for i in range(0,10):
    print(N.count(i))

