def solution(n, s, a, b, fares):
    from heapq import heappop, heappush
    from collections import defaultdict
    
    INF = float('inf')
    answer = INF
    DBG = False
    
    def dijkstra(init_node):
            # A dijkstra
            fist = [INF] * (n+1)
            hq = [(0, init_node)]
            fist[init_node] = 0

            while hq:
                cur_dist, cur_node = heappop(hq)

                if cur_dist > fist[cur_node]:
                    continue
                fist[cur_node] = cur_dist

                for nxt_node, d in edges[cur_node]:

                    nxt_dist = cur_dist + d
                    if nxt_dist <= dist[nxt_node]:
                        heappush(hq, (nxt_dist, nxt_node))
            
            return fist
    """
    1. 둘이 따로 경로 기록하면서 dijkstra + 나중에 후처리로 경로 합치기
    2. dijkstra 한번 + 결과 배열 각 지점부터 따로 각자 목적지로 dijkstra
    2번 같은데, floid washall 비슷한 것인가 그건 bfs 여러번 돌리는 거였나
    """
    
    # initialize: 양방향 + 중복 없음
    # arr = [[0]*(n+1) for _ in range(n+1)]
    edges = defaultdict(list)
    
    for c, d, f in fares:
        # arr[c][d] = f
        # arr[d][c] = f
        edges[c].append((d, f))
        edges[d].append((c, f))
    
    dist = [INF] * (n+1)
    dist[s] = 0
    
    # 기본 dijkstra
    hq = [(0, s)]
    
    while hq:
        cd, cn = heappop(hq)
        if cd > dist[cn]:   # 여기 >= 아닌 게 맞나?
            continue
        dist[cn] = cd
        
        for nn, d in edges[cn]:
            if not d: continue
            nd = cd + d
            
            if nd <= dist[nn]:
                heappush(hq, (nd, nn))
    
    if DBG: print(n, dist)
    
    for init_node in range(1, n+1):
        if DBG: print(f'init node: {init_node}, init dist: {dist[init_node]}')
        # if init_node == s: continue # 이거 있으면 안됨. 시작점에서 바로 갈라지는 것도 포함이라
        
        init_dist = dist[init_node]
        fist = dijkstra(init_node)
        cost_A = fist[a]
        cost_B = fist[b]
        
        if DBG:
            print(cost_A, dist_A)
            print(cost_B, dist_B)
            print()
        
        answer = min(answer, init_dist + cost_A + cost_B)
    
        
    return answer