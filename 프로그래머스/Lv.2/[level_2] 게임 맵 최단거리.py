
from collections import deque
def solution(maps):
    answer = -1

    def bfs(maps, y, x, distance, visited):
        queue = deque([(y,x,distance)])
        visited[y][x] = True
        dy = [-1, 1, 0, 0] # 위 아래
        dx = [0, 0, -1, 1] # 왼쪽 오른쪽

        while queue:
            v = queue.popleft()
            print(v, end = '')
            for i in range(4):
                ny = v[0] + dy[i]
                nx = v[1] + dx[i]
                if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]):
                    if maps[ny][nx] == 1:
                        if visited[ny][nx] == False:
                            distance = v[2] + 1
                            queue.append((ny,nx,distance))
                            visited[ny][nx] = True
                            if ny == len(maps)-1 and nx == len(maps[0])-1:
                                print(distance)
                                return distance 
        return -1

    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    answer = bfs(maps,0,0,1,visited) 
    # 처음 설정한 불필요 코드 같이 제출됨
    return answer

maps	= [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
solution(maps)
