# 2. https://www.acmicpc.net/problem/10869 : 사칙연산
A, B = map(int, input().split())
A >= 0
B <= 10,000
print(int(A+B))
print(int(A-B))
print(int(A*B))
print(int(A/B))
print(int(A%B))