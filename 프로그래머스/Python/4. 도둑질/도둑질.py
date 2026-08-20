def myp(arr):
    for row in arr:
        for val in row:
            print(f'{val:>2}', end=' ')
        print()
    print()

def solution(money):
    answer = 0
    N = len(money)
    
    """
    인접한 두 집을 터면 안됨
    예외 상황은 배열 기준 마지막이랑 처음
    
    dp[i][j] = i번째 집까지 보고 i번째 집을 털었거나 (j=1) 안털었을 때 (j=0) 훔친 돈 최댓값
    이걸 dp0을 첫번째 집을 안턴 경우, dp1을 첫번째 집을 턴 경우로 나눠서 하자
    """
    
    dp0 = [[-1]*2 for _ in range(N)]
    dp1 = [[-1]*2 for _ in range(N)]
    
    dp0[0][0] = 0
    dp1[0][1] = money[0]
    
    for i in range(N-1):
        # 털자
        dp0[i+1][1] = max(dp0[i+1][1], dp0[i][0] + money[i+1])
        if dp1[i][0] != -1:
            dp1[i+1][1] = max(dp1[i+1][1], dp1[i][0] + money[i+1])
                
        # 털지 말자
        dp0[i+1][0] = max(dp0[i+1][0], dp0[i][1], dp0[i][0])
        dp1[i+1][0] = max(dp1[i+1][0], dp1[i][1], dp1[i][0])
    
    return max(max(dp0[-1]), dp1[-1][0])
