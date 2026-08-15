from collections import deque
def solution(progresses, speeds):
    N = len(speeds)
    q = deque()
    
    for i in range(N):
        q.append(i)
    
    done = [0] * N
    clst = []
    while q:
        for i in range(N):
            if done[i]:
                continue
            progresses[i] += speeds[i]
            if progresses[i] >= 100:
                done[i] = 1
        
        cnt = 0
        while q and done[q[0]] == 1:
            q.popleft()
            cnt += 1
        if cnt > 0:
            clst.append(cnt)
        
    return clst