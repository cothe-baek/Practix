def myp(arr):
    for row in arr:
        for val in row:
            print(val, end=' ')
        print()
    print()


def solution(M, N, puddles):
    """
    dp[i][j] = i, j로 가는 최단 경로의 개수
    """
    arr = [[0] * M for _ in range(N)]
    for i, j in puddles:
        arr[j-1][i-1] = 1
    
    dp = [[0]*M for _ in range(N)]
    dp[0][0] = 1
    
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                continue
                
            # 오른쪽
            if j < M-1 and arr[i][j+1] == 0:
                dp[i][j+1] += dp[i][j]
            
            # 아래
            if i < N-1 and arr[i+1][j] == 0:
                dp[i+1][j] += dp[i][j]
    
    myp(dp)
    
    return dp[N-1][M-1] % 1000000007