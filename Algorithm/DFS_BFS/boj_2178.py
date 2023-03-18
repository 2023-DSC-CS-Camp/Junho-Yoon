import sys,math,time
from collections import deque

n, m = list(map(int, sys.stdin.readline().split()))
maze = [list(input())[:] for _ in range(n)]
# (x,y)
movement = [(1,0),(0,-1),(-1,0),(0,1)]
# 시작점을 정수형으로 변환해서 대입
maze[0][0] = 1
# BFS Queue에 첫 좌표를 넣는다.
q = deque([(0,0)])

while q:
    x,y = q.popleft()
    for a,b in movement:
        new_x = x + a
        new_y = y + b
        if (new_x >= 0 and new_x < m) and (new_y >= 0 and new_y < n) and maze[new_y][new_x] == '1':
            q.append((new_x,new_y))
            maze[new_y][new_x] = maze[y][x] + 1
print(maze[n-1][m-1])