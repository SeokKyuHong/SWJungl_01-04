import sys
sys.stdin = open("input.txt","r")
#11. https://www.acmicpc.net/problem/2562 : 최댓값
# max_list=list(map(int, input().split()))
max_list=list(int(sys.stdin.readline()) for i in range(9))

max_n = max(max_list)
#최댓값
print(max_n)
#최댓값이 몇번째인지
for i in range(len(max_list)):
    if max_n <= max_list[i]:
        print(max_list.index(max_n)+1)