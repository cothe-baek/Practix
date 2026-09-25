def solution(s):
    N = len(s)
    answer = N
    
    """
    길이 반까지만 확인하면 되지 않나
    길이 8인데 5개 단위 압축을 하면 반복이 생길 수가 없음
    그럼 500 x 1000 정도
    """
    
    for unit in range(1, N//2+1):
        prev = s[:unit]
        tmp, stack = 0, 1
        suppressed = ""
        for i in range(unit, N, unit):
            if i+unit <= N:
                cur = s[i:i+unit]
            else:
                cur = s[i:]
            
            # print('prev:', prev, 'cur:', cur)
            
            if cur == prev:
                stack += 1
            else:
                if stack > 1:
                    tmp += unit + len(str(stack))
                    suppressed += str(stack) + prev
                    stack = 1
                else:
                    tmp += unit
                    suppressed += prev
            prev = cur
        
        # print(suppressed)
        if stack > 1:
            tmp += len(cur) + len(str(stack))
            suppressed += str(stack) + cur
            stack = 1
        else:
            tmp += len(cur)
            suppressed += cur
        
        # print(suppressed)
        if tmp < answer:
            answer = tmp
                
        
    return answer