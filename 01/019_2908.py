import sys
sys.stdin = open("input.txt","r")
# 19.https://www.acmicpc.net/problem/2908 : 상수
AB = list(map(str, input().split()))
A = AB[0]
B = AB[1]
A_list = list(A)
B_list = list(B)

A_S = list(A_list[2] + A_list[1] + A_list[0])#문자열 반대로
B_S = list(B_list[2] + B_list[1] + B_list[0])#문자열 반대로
if A_S > B_S :
    print(A_S[0]+A_S[1]+A_S[2])
else:
    print(B_S[0]+B_S[1]+B_S[2])


