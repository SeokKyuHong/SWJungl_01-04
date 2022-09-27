import sys
from itertools import permutations
sys.stdin = open("input.txt","r")
# 37.https://www.acmicpc.net/problem/10819 :차이를 최대로
input=sys.stdin.readline

N = int(input())
card_list = list(map(int, input().split(' ')))
# card_list.sort()

dab_list=[]
Q = []
dab_list=list(permutations(card_list, N))
# print(dab_list)
for i in range(len(dab_list)):
    for j in range(len(dab_list[i])):
        U = dab_list
        
        Y = []
    
        for u in range(len(dab_list[i])-1):
            a = abs(U[i][j-(u)]-U[i][j-(u+1)])
            
            Y.append(a)

    
    for n in range(len(Y)):
        e=sum(Y)
        Q.append(e) 
print(max(Q))    
            

        