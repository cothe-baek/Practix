from collections import OrderedDict
def solution(cacheSize, cities):
    cache = OrderedDict()
    answer = 0
    
    for i, city in enumerate(cities):
        city = city.lower()
        
        if city in cache:
            answer += 1
            cache.move_to_end(city)
        else:
            answer += 5
        
        cache[city] = i
        # print(cache)
        while len(cache) > cacheSize:
            cache.popitem(last=False)
            
    return answer