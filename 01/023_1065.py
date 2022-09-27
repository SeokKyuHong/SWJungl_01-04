import sys
sys.stdin = open("input.txt","r")
# # 23.https://www.acmicpc.net/problem/1065 : 한수
N = input()#문자임
# print(N[0])#문자임
count1 = 0 # 1~N 까지의 모든 수를 리스트로 만들기 위해
count2 = 99 # 리스트에서 3자리의 수 중 한수를 리스트하기위해
count3 = 0 # 3자리의 한수를 카운팅 하기 위해
N_list = [] # 1~N 까지 리스트 
N_list2 = [] # 3자리의 한수를 담기 위한 리스트 

# 1~N 을 리스트로 뽑음
for i in range(int(N)):
    count1 += 1
    N_list.append(str(count1))
# print(N_list)

#N이 두자리면 무조건 한수 이므로 그냥 출력
if len(N_list) <= 99:
    print(len(N_list))

# N 이 3자리면 한수를 찾아야함
elif len(N_list) >= 100:
    for i in range(100, int(N)+1):
        count2 += 1
        N_list2.append(str(count2)) 
    # print(N_list2)# 3자리 수를 리스트로 담음

    for j in range(0, int(len(N_list2))):
        A = N_list2[j]
        
        if int(A[0])-int(A[1]) == int(A[1])-int(A[2]):
            count3 += 1
    print(count3+99)
            


        

