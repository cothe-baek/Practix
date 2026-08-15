def solution(prices):
    N = len(prices)
    from collections import deque
    answer = [0]*N
    """
    하나씩 넣으면서 가장 최근에 넣은 값보다 작은 걸 발견하면 하나씩 pop하면서 시간 계산
    """
    q = deque()
    for i in range(N):
        cur = prices[i]
        
        while True:
            if q and cur < q[-1][1]:
                pi, pp = q.pop()
                # print('time:', i, '/ popped:', pi, pp)
                answer[pi] = i - pi
            else:
                break
        
        q.append((i, cur))
        # print(q)
            
    while q:
        pi, pp = q.pop()
        answer[pi] = N-1 - pi
        
    return answer