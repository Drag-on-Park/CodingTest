def solution(m, n, startX, startY, balls):
    answer = []
    symmetry = []
    distance = []
    # balls 4개의 대칭점
    # 반전 상/하/좌/우
    for i,j in balls:
        # 매번 초기화
        symmetry = []

        # 상
        if not (i == startX and startY < j):
          symmetry.append((i,2*n-j))
        # 하
        if not (i == startX and startY > j):
          symmetry.append((i,-j))
        # 좌
        if not (i < startX and j == startY):
          symmetry.append((-i,j))
        # 우
        if not (i > startX and j == startY):
          symmetry.append((2*m-i,j))

        # answer = min(distance = (a[0]-startX)**2+(a[1]-startY)**2)
        distance = min((x-startX)**2 + (y-startY)**2 for x,y in symmetry)
        answer.append(distance)
    return answer


#가로
m = 10
#세로
n = 10
startX = 3
startY = 7
balls =	[[7, 7], [2, 7], [7, 3]]
# return [52, 37, 116]
solution(m, n, startX, startY, balls)