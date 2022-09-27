import sys, math
sys.stdin = open("input.txt","r")
# 21.https://www.acmicpc.net/problem/1978 : 소수 찾기
N = int(input())
list = list(map(int, input().split(" ")))

def is_prime_num(n):
    arr = [True] * (n + 1)
    arr[0] = False
    arr[1] = False

    for i in range(2, int(math.sqrt(n)+1)):
        if arr[i] == True:
            j = 2

            while (i * j) <= n:
                arr[i*j] = False
                j += 1

    return arr

arr = is_prime_num(max(list))
LLL= []
for i in range(len(arr)):
    if arr[i] == True:
        LLL += [i]
print(LLL)
III=[i for i in LLL if i in list]

print(len(III))
        