import sys
sys.stdin = open("input.txt","r")
#6. https://www.acmicpc.net/problem/1085 : 직사각형에서 탈출
x, y, w, h  = map(int, input().split())
x_m = w-x
y_m = h-y
list = [x_m,x,y_m,y]
print(min(list))