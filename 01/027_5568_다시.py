import sys
from itertools import permutations
sys.stdin = open("input.txt","r")
# 27. https://www.acmicpc.net/problem/5568 : 카드놓기

input = sys.stdin.readline
n = int(input())
k = int(input())
cards = [input().rstrip() for _ in range(n)]
# 같은 조합이라도 순서에 따라 다른 수 -> 순열
nums = set()
for num_set in permutations(cards,k):
    nums.add(''.join(num_set))
print(len(nums))