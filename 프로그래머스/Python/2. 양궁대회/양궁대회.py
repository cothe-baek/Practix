def solution(N, info):
    answer = [-1]
    mx_diff = 1
    
    """
    가장 큰 점수차로 이겨야 함
    시간복잡도는
    총 11개 점수에 대해 매번 승리 or 넘어가기 니까 2^11
    점수계산을 매번 하니까 x11
    대충 2만번 좀 넘음
    """
    ryan = [0]*11
    def dfs(n, idx):
        nonlocal mx_diff, answer
        
        if idx == 11:
            ry_score, ap_score = 0, 0
            for i in range(10):
                if ryan[i] > info[i]:
                    ry_score += 10-i
                elif info[i] > 0 and info[i] >= ryan[i]:
                    ap_score += 10-i
            
            # 점수차 더 크면 아묻따 정답
            if ry_score - ap_score > mx_diff:
                # print(ry_score, ap_score, ryan)
                answer = ryan[:]
                mx_diff = ry_score - ap_score
            
            # 같으면 역순탐색 선착순
            elif ry_score - ap_score == mx_diff:
                if answer == [-1]:
                    answer = ryan[:]
                    return
                
                for i in range(10, -1, -1):
                    if ryan[i] > answer[i]:
                        answer = ryan[:]
                        return
                    if ryan[i] < answer[i]:
                        return
            return
    
        # 마지막이면 남은 거 털어넣기
        if idx == 10:
            ryan[idx] = n
            dfs(0, idx+1)
            ryan[idx] = 0
        
        else:
            # 이번 점수 과녁에서 승리
            if n > info[idx]:
                ryan[idx] = info[idx] + 1
                dfs(n - ryan[idx], idx + 1)
                ryan[idx] = 0

            # 줄건 줘
            dfs(n, idx + 1)
        
    dfs(N, 0)
    
    return answer