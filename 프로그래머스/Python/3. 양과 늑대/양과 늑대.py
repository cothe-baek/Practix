def solution(info, edges_):
    answer = 0
    from collections import defaultdict
    
    edges = defaultdict(list)
    for a, b in edges_:
        edges[a].append(b)
        edges[b].append(a)
    
    mask = 1
    lst = [1, 0]
    v = set()
    
    def dfs(n, mask):
        nonlocal answer
        
        if lst[0] <= lst[1]:
            return
        if (n, mask) in v:
            return
        
        v.add((n, mask))
        
        answer = max(answer, lst[0])
        
        for nxt in edges[n]:
            if (mask & 1<<nxt) == 0:
                lst[info[nxt]] += 1
            dfs(nxt, mask | 1<<nxt)
            if (mask & 1<<nxt) == 0:
                lst[info[nxt]] -= 1
        
    dfs(0, 1)
    
    
    return answer