def solution(hq, K):
    answer = 0
    import heapq as hf
    
    hf.heapify(hq)
    
    # 제일 낮은 두개 꺼내고 더하기
    while len(hq) > 1 and hq[0] < K:
        val = hf.heappop(hq) + hf.heappop(hq) * 2
        hf.heappush(hq, val)
        answer += 1
    
    if hq[0] < K:
        return -1
    else:
        return answer