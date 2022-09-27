
import sys, math
sys.stdin = open("input.txt","r")
# 20.https://www.acmicpc.net/problem/2869 : 달팽이는 올라가고 싶다
ABV = list(map(int, sys.stdin.readline().split()))
A = ABV[0]
B = ABV[1]
V = ABV[2]
N = 0
day1 = A-B

if (V-B)%(A-B) == 0:
    print(math.ceil((V-B)/(A-B)))
else:
    print(math.ceil((V-B)/(A-B)))
 










