from collections import deque
from heapq import heappush, heappop

def solution(N, road, K):
    answer = 0

    arr = [[0] * (N+1) for _ in range(N+1)]
    
    for i, j, time in road:
        if arr[i][j] > 0:
            arr[i][j] = min(arr[i][j], time)
            arr[j][i] = min(arr[j][i], time)
        else:
            arr[i][j] = time
            arr[j][i] = time
    
    hq = []
    v = [0] * (N+1)
    
    hq.append((0, 1))
    
    while hq:
        ct, ci = heappop(hq)
        
        if v[ci]:
            continue
        
        v[ci] = 1
        # print(ci, ct)

        answer += 1
        
        for ni in range(2, N+1):
            if not v[ni] and 0 < arr[ci][ni] <= K-ct:
                heappush(hq, (arr[ci][ni] + ct, ni))
            

    return answer