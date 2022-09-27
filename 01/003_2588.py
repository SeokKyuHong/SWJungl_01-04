import sys
sys.stdin = open("input.txt","r")
# 3. https://www.acmicpc.net/problem/2588 : 곱셈
a = int(input())
b = int(input())
print(int(a*int(str(b)[2])))
print(int(a*int(str(b)[1])))
print(int(a*int(str(b)[0])))
print(int(a*b))


