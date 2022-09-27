import sys
sys.stdin = open("input.txt","r")
# 24.https://www.acmicpc.net/problem/2628 : 종이 자르기

W, H = map(int, input().split())#W 가로 길이, H 세로길이
T = int(input()) #케이스(점 개수)

h_list = []#세로의 길이를 비교하기 위한 빈 리스트
w_list = []#가로의 길이를 비교하기 위한 빈 리스트 

# 케이스의 개수대로 값 받기
# P가 0이면 (가로로 자르는)세로의 길이, P가 1 이면 (세로로 자르는)가로 길이
for _ in range(T):
    P, D = map(int, input().split())
#-----모든 세로, 가로값을 리스트로 가져옴-------
    if P == 0 :#세로의 길이
        h_list.append(D) 

    else:#가로의 길이
        w_list.append(D)
#---작은 순으로 정렬----
h_list.append(H)
h_list.append(0)
w_list.append(W)
w_list.append(0)                
h_list.sort()  
w_list.sort() 
print(h_list)
print(w_list)
#---사각형들 넓이 구하기
S = [] # 사각형 넓이 리스트
#세로높이가 같은 사각형들
for i in range(len(h_list)-1):
    for j in range(len(w_list)-1):
        if w_list[j-1] == W and h_list[i-1] == H:
            S.append((h_list[i-1]-h_list[i-2]) * (w_list[j-1]-w_list[j-2]))

        else:
            S.append((h_list[i+1]-h_list[i]) * (w_list[j+1]-w_list[j]))
                   
print(max(S))
    
 