import sys
sys.stdin = open("input.txt","r")

#9. https://www.acmicpc.net/problem/2438 : 별찍기
N = int(input())
for i in range(0, N):
    for a in range(i+1):
        print("*", end='')
    print("")   
    