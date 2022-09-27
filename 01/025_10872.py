import sys
sys.stdin = open("input.txt","r")
# 25.https://www.acmicpc.net/problem/10872 : 팩토리얼
def factorial(T):
    if T == 1:
        return 1
    return T * factorial(T-1)

print(factorial(int(input())))

