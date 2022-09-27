import sys
sys.stdin = open("input.txt","r")
# 4. https://www.acmicpc.net/problem/9498 : 시험성적
test = int(input())
if 90 <= test <= 100:
    print('A')
elif 80 <= test <= 89:
    print('B')
elif 70 <= test <= 79:
    print('C')
elif 60 <= test <= 69:
    print('D')
else:
    print('F')
