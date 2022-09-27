import sys
sys.stdin = open("input.txt","r")
# 34.https://www.acmicpc.net/problem/1181 :단어 정렬
input=sys.stdin.readline

list=[]
N = int(input())
for i in range(N):
    a = input().split()
    list += a

list.sort(key=len)

for i in range(N):
    if list == len(list[i]):
        print(list)

bin=[]
for i in list:
    if i not in bin:
        bin.append(i)
bin.sort()
bin.sort(key=lambda x:len(x))

for i in range(len(bin)):

    print(bin[i])

# case=int(input())
# tila=list()
# newtila=list()
# for i in range(case):
#     a=str(input())
#     tila.append(a)
# for j in tila:
#     if j not in newtila:
#         newtila.append(j)
# newtila.sort()
# newtila.sort(key=lambda x:len(x))
# for l in range(len(newtila)):
#     print(newtila[l])