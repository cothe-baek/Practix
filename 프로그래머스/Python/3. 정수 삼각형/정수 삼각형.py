def myp(arr):
    for row in arr:
        for val in row:
            print(val, end=' ')
        print()
    print()
    
def solution(tri):
    N = len(tri)
    arr = [[0]*N for _ in range(N)]
    
    for i in range(N):
        for j in range(i+1):
            arr[i][j] = tri[i][j]
    # myp(arr)
    
    """
    dp[i][j]: 거쳐간 숫자의 합의 최댓값
    
    이런 문제는 일단 0,0을 두면 좋은가 나쁜가
    """
    dp = [[-1]*N for _ in range(N)]
    dp[0][0] = arr[0][0]
    
    for i in range(N-1):
        for j in range(N-1):
            # 아래로
            dp[i+1][j] = max(dp[i+1][j], dp[i][j] + arr[i+1][j])
            # 오른쪽 아래로
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + arr[i+1][j+1])
    
    return max(dp[N-1])