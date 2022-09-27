import sys
sys.stdin = open("input.txt","r")
# 18.https://www.acmicpc.net/problem/1152 : 단어의 개수
num_list = list(map(str, input().split()))
print(len(num_list))