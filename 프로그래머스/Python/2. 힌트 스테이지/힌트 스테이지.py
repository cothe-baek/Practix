def solve(cost, bundle):
    DBG = True

    answer = float('inf')
    N, K = len(cost), len(bundle[0]) - 1
    hint_ticket = [0] * N
    
    """
    1~N 힌트권
    i번 힌트권은 i번 스테이지에서만 사용
    한 스테이지에서 최대 n-1개 사용 가능
    
    스테이지마다 판매하는 힌트 번들 구매 가능 (마지막 스테이지 제외)
    이후 스테이지의 힌트권이 있음
    
    dfs
    """
    
    def dfs(cur_cost, n):
        nonlocal answer
        
        if n == N-1: # 마지막 스테이지는 힌트 있으면 써야지
            answer = min(answer, cur_cost + cost[n][min(N-1, hint_ticket[n])])
            return
        
        # 현재 스테이지 n
        solve_cost = cost[n][min(N-1, hint_ticket[n])]
        
        # 힌트 안사고 넘어가기
        dfs(cur_cost + solve_cost, n+1)
        
        # 힌트 사고 넘어가기
        hint_cost = bundle[n][0]
        
        for k in range(1, K+1):
            hint_ticket[bundle[n][k] - 1] += 1
        
        dfs(cur_cost + solve_cost + hint_cost, n+1)
        
        for k in range(1, K+1):
            hint_ticket[bundle[n][k] - 1] -= 1
        
    dfs(0, 0)
        
    return answer

def solution(*args):
    import traceback
    try:
        return solve(*args)
    except Exception as e:
        tb = traceback.extract_tb(e.__traceback__, limit=100)[-1]
        return f"{type(e).__name__} | line {tb.lineno} | {tb.line}"

    