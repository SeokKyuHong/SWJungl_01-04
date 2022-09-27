
import sys
sys.stdin = open("input.txt","r")
# 27. https://www.acmicpc.net/problem/1914 : 히노이 탑
N = int(input())
count1 = 0
count2 = 0
count3 = 0
print((2**N)-1)
def hanoi(n, 출발, 경유, 목적):
    if n == 1:
        return count3

