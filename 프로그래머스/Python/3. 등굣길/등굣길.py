def solution(M, N, puddles):
    answer = 0
    
    arr = [[0]*M for _ in range(N)]
    dp = [[0]*M for _ in range(N)]
    dp[0][0] = 1
    
    for j, i in puddles:
        arr[i-1][j-1] = 1
    
    for i in range(N):
        for j in range(M):
            # 오른쪽
            if j < M-1 and not arr[i][j+1]:
                dp[i][j+1] = dp[i][j+1] + dp[i][j]
            
            # 아래쪽
            if i < N-1 and not arr[i+1][j]:
                dp[i+1][j] = dp[i+1][j] + dp[i][j]
    
    
    return dp[N-1][M-1] % (10**9 + 7)