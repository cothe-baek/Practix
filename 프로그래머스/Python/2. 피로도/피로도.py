def solution(k, dungeons):
    answer, cnt  = 0, 0
    N = len(dungeons)
    v = [0] * N
    
    def dfs(n, cur, cnt):
        nonlocal answer
        # print(v, cur)
        
        if cnt > answer:
            answer = cnt
        
        for i in range(N):
            if not v[i] and cur >= dungeons[i][0]:
                v[i] = 1
                # print('going to:', i+1, 'th dungeon')
                dfs(i+1, cur-dungeons[i][1], cnt + 1)
                v[i] = 0
    
    dfs(0, k, 0)
        
    
    return answer