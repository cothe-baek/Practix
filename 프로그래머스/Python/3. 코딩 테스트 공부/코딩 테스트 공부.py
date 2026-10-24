from heapq import heappop, heappush
import traceback
DBG = False

def solve(alp, cop, problems):
    INF = float('inf')
    answer = INF
    N = len(problems)
    """
    이거도 dijkstra 아닌가
    그냥 모든 문제들 돌면서 그 문제 풀었을 때 증가하는 비용 반영하고
    지금 못푸는 문제면 그냥 알고력이나 코딩력 부족한만큼 시간 더하고
    어 근데 같은 문제를 여러번 풀 수도 있네
    """
    mx_alp = max([x[0] for x in problems])
    mx_cop = max([x[1] for x in problems])
    alp, cop = min(mx_alp, alp), min(mx_cop, cop)
    
    dist = [[INF] * (mx_cop + 1) for _ in range(mx_alp + 1)]
    dist[alp][cop] = 0
    dist[mx_alp][mx_cop] = max(0, mx_alp - alp) + max(0, mx_cop - cop)
    
    hq = [(0, alp, cop)]
    
    while hq:
        cur_cost, cur_alp, cur_cop = heappop(hq)
        if DBG: print(cur_cost, cur_alp, cur_cop)
        
        if cur_cost > dist[cur_alp][cur_cop]:
            continue
        if cur_alp >= mx_alp and cur_cop >= mx_cop:
            continue
        
        for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
            res_alp = max(0, alp_req - cur_alp)
            res_cop = max(0, cop_req - cur_cop)
            
            nxt_cost = cur_cost + res_alp + res_cop + cost
            nxt_alp, nxt_cop = cur_alp + res_alp + alp_rwd, cur_cop + res_cop + cop_rwd
            nxt_alp, nxt_cop = min(mx_alp, nxt_alp), min(mx_cop, nxt_cop)
            
            if nxt_cost < dist[nxt_alp][nxt_cop]:
                heappush(hq, (nxt_cost, nxt_alp, nxt_cop))
                dist[nxt_alp][nxt_cop] = nxt_cost
    
    # 최단시간 구하기
    for i in range(mx_alp+1):
        for j in range(mx_cop+1):
            if dist[i][j] == INF:
                continue
            res_cost = mx_alp - i + mx_cop - j
            
            if dist[i][j] + res_cost < answer:
                answer = dist[i][j] + res_cost
    
    return answer


def solution(alp, cop, problems):
    try:
        return solve(alp, cop, problems)
    except Exception:
        return traceback.format_exc()