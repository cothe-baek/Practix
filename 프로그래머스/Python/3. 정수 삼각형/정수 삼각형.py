"""
dp[i][j]: i, j까지 왔을 때 거쳐온 숫자의 합 최댓값
"""

def solution(triangle):
    answer = 0
    N = len(triangle)
    
    arr = [[0]*N for _ in range(N)]
    dp = [[0]*(N) for _ in range(N)]
    
    for i in range(N):
        for j in range(i+1):
            arr[i][j] = triangle[i][j]
    
    dp[0][0] = arr[0][0]
    for i in range(N-1):
        for j in range(i+1):
            # 아래로 이동
            dp[i+1][j] = max(dp[i+1][j], dp[i][j] + arr[i+1][j])
            # 오른쪽 아래로 이동
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + arr[i+1][j+1])
            
    answer = max(dp[-1])
        
    
    # for row in dp:
    #     for val in row:
    #         print(f"{val:>2}", end=" ")
    #     print()
    # print()
    
    return answer