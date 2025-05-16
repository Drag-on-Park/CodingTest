import heapq

def solution(scoville, K):
    heap = []
    answer = 0
    mix_scoville = 0
    temp = 0

    for i in scoville:
        heapq.heappush(heap,i)


    while len(heap)>=2 and heap[0] < K:
        if heap[0] < K:
            temp = heapq.heappop(heap)
            mix_scoville = temp + (heap[0]*2)
            heapq.heappop(heap)
            heapq.heappush(heap,mix_scoville)
            answer += 1
    if heap[0] >= K:
          print(answer)
          return answer
    else:
          return -1

scoville = [1, 2, 3, 9, 10, 12]
K = 7
# #return 2
solution(scoville, K)