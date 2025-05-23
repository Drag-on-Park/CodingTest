from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    def one_diff(a, b):
        count = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                count += 1
        return count == 1

    answer = 0
    queue = deque([(begin,0)])
    visited = {i:False for i in words}

    while queue:
          v, steps = queue.popleft()
          if v == target:
              print(answer)
              return steps

          for one in words:
              if one_diff(one, v) and not visited[one]:
                    visited[one] = True
                    print(visited)
                    queue.append((one, steps+1))
                    print(queue)
    
    return 0

      # 한번에 한글자
      # 최종 타겟

begin = "hit"
target = "cog"
words = 	["hot", "dot", "dog", "lot", "log", "cog"]
# return 4

# begin = "hit"
# target = "cog"
# words = 	["hot", "dot", "dog", "lot", "log"]
# # return 0

solution(begin, target, words)