def solution(priorities, pos):
    from collections import deque
    N = len(priorities)
    max_p = max(priorities)
    q = deque()
    
    pset = set()
    plst = [0] * 10
    
    for i in range(N):
        q.append((i, priorities[i]))
        plst[priorities[i]] += 1
        pset.add(priorities[i])
    
    cnt = 0
    while q:
        ci, cp = q.popleft()
        if cp < max_p:
            q.append((ci, cp))
        
        else:
            plst[max_p] -= 1
            if plst[max_p] == 0:
                pset.remove(max_p)
                if pset:
                    max_p = max(pset)
            
            cnt += 1
            if ci == pos:
                return cnt