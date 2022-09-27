import sys
sys.stdin = open("input.txt","r")
# 17.https://www.acmicpc.net/problem/2675 : 문자열반복
T = int(sys.stdin.readline())
for i in range(T):
    P = list(map(str, input().split()))
    
    O = ""
    for j in range(len(P[1])):
        Y = ""
        for u in range(int(P[0])):
            
            Y = Y + str(P[1][j])
        
        O = O + Y
    print(O)


        
    