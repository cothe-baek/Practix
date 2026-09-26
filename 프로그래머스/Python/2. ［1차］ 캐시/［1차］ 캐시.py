def solution(cacheSize, cities):
    import heapq
    cache = {}
    hq = []
    answer = 0
    
    for i, city in enumerate(cities):
        city = city.lower()
        if city in cache:
            answer += 1
        else:
            answer += 5
        
        heapq.heappush(hq, (i, city))
        cache[city] = i
        
        if len(cache) > cacheSize:
            while True:
                pop_i, pop_city = heapq.heappop(hq)
                # 유요한 걸 pop하고 처리하기
                if pop_city not in cache or cache[pop_city] == pop_i:
                    del cache[pop_city]
                    break
        
            
    return answer