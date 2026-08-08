"""
dp[i]: N을 i번 사용해서 number를 만들 수 있는지
dp[i][j]: N을 i번 사용해 j를 만들 수 있는지
얘넨 탈락

dp[i]: N을 사용해 i를 만들 수 있는 최소 개수
당첨이 아니네용 괄호 연산을 위해서는

dp[i]: N을 i번 사용해 만들 수 있는 수들의 집합
을 사용해야 한다고 하네요

이러면 dp[i+j]: dp[i] 와 dp[j]의 연산으로 나올 수 있는 수들의 집합
주의할 건, 이렇게 push로 할거면 i루프 안의 j 루프를 ~i까지로 해야 한다는 거
그렇게 안하면 완성되지 않은 dp 칸을 사용해 다음 dp값을 계산하는 불상사가 발생함

pull로 할거면 dp[i]: = dp[j] + dp[i-j] 로 하면 되는데, 이건 불상사 생각 안해도 되는 듯
대신 이때 종료조건 위치랑 어차피 1,3 / 2,2 / 3,1 처럼 바뀐 상황을 자동으로 계산하니
아래 push처럼 n, m 자리바꿈 계산은 안해도 됨
"""

def solution(N, number):
    answer = 10
    
    dp = [set() for _ in range(9)]
    # dp[0].add(0)
    
    for i in range(1, 5):
        dp[i].add(int(str(N)*i))
    
    for i in range(1, 9):
        if number in dp[i]:
            return i
        
        for j in range(1, i+1):
            if i + j > 8:
                continue
                
            for n in dp[j]:
                for m in dp[i]:
                    if n - m > 0:
                        dp[i+j].add(n - m)
                    elif m - n > 0:
                        dp[i+j].add(m - n)
                    dp[i+j].add(n + m)
                    dp[i+j].add(n * m)
                    if m > 0:
                        dp[i+j].add(n / m)
                    if n > 0:
                        dp[i+j].add(m / n)
            
    return -1
