import sys
from itertools import combinations
sys.stdin = open("input.txt","r")
# 36.https://www.acmicpc.net/problem/2798 :블랙잭
input=sys.stdin.readline

N, M = map(int, input().split())
card_list = list(map(int, input().split(' ')))
result=list(combinations(card_list,3))

# def card():
#     for i in range(len(result)):
#         sum(result[i])
    

# for i in range(len(result)):
#     if sum(result[i]) == M:
#         print(result[i])
card_sum = []
for i in range(len(result)):
    card_list.append(sum(result[i]))
card_list.sort()

card_pic = []
for i in range(len(card_list)):
    if card_list[i] <= M:
        card_pic.append(card_list[i])
print(max(card_pic))