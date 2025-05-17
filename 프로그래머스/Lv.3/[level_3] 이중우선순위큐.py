import heapq
def solution(operations):
    answer = []
    max_heap = []
    result = []

    for i in operations:
        temp = i.split()
        if temp[0] == 'I':
            heapq.heappush(answer, int(temp[1]))
        elif temp[0] == 'D':
            if temp[1] == '-1':
                if not answer:
                    continue
                # 최솟값
                heapq.heappop(answer)
            elif temp[1] == '1':
                if not answer:
                    continue
                max_heap = []
                # 최댓값 
                for num in answer:
                    heapq.heappush(max_heap, (-int(num), int(num)))
                heapq.heappop(max_heap)
                answer = []
                for i in max_heap:
                    heapq.heappush(answer,i[1])

    if not answer:
        return [0,0]

    result_temp = []
    for i in answer:
        heapq.heappush(result_temp, (-int(i), int(i)))
    result_max = heapq.heappop(result_temp)
    result.append(result_max[1])

    result.append(heapq.heappop(answer))
    
    
    return result

operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
#  return [333, -45]
print(solution(operations))
