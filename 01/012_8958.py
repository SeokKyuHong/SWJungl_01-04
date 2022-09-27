import sys
sys.stdin = open("input.txt","r")
# 12. https://www.acmicpc.net/problem/8958 : OX
T = int(sys.stdin.readline())
for i in range(T):
    N = list(input())
    counting = 0
    tcounting = 0
    for i in range(len(N)):
        if N[i] == 'O':
            counting += 1
            tcounting += counting
        else:
            counting = 0
    print(tcounting)





