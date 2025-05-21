def solution(cacheSize, cities):
  cache = []
  answer = 0
  hit = 1
  miss = 5

  for i in cities:
    i = i.lower()
    
    if len(cache) == cacheSize:
      if cacheSize == 0:
        answer += miss
        continue

      elif i in cache:
        cache.remove(i)
        answer += hit
        cache.append(i)
        continue

      else:
        cache.remove(cache[0])
        cache.append(i)
        answer += miss
        continue
      
    if i in cache:
      cache.remove(i)
      answer += hit
      cache.append(i)
      continue

    cache.append(i)
    answer += miss
  
  print(answer)
  return answer


cacheSize = 3
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
solution(cacheSize, cities)