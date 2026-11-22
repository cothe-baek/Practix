def solution(routes):
    routes = sorted(routes, key=lambda x: x[1])
    
    # print(routes)
    
    cam = None
    cnt = 0
    for s, e in routes:
        if cam is None or not (s <= cam <= e):
            cam = e
            cnt += 1
    
    return cnt