def solution(operations):
    import heapq as hf
    
    minq = []
    maxq = []
    
    v = set()
    idx = 0
    for op in operations:
        cmd, val = op.split()
        val = int(val)
        
        if cmd == 'I':
            idx += 1
            hf.heappush(minq, (val, idx))
            hf.heappush(maxq, (-val, idx))
            v.add(idx)

        elif cmd == 'D':
            if val == -1:
                # 먼저 v에 없는 값(삭제된 값)들을 빼내기
                while minq and minq[0][1] not in v:
                    hf.heappop(minq)
                # 유효한 값에서 min값 삭제 수행
                if minq:
                    num, i = hf.heappop(minq)
                    v.remove(i)
                        
            
            elif val == 1:
                while maxq and maxq[0][1] not in v:
                    hf.heappop(maxq)
                
                if maxq:
                    num, i = hf.heappop(maxq)
                    v.remove(i)
                    
#         print(f"명령어: {op}")
        
#         # [1] 큐의 현재 상태 (maxq는 부호 반전)
#         print(f"minq 상태: {[(val, idx) for val, idx in minq]}")
#         print(f"maxq 상태: {[(-val, idx) for val, idx in maxq]}")
        
#         # [2] 유효 인덱스(v)를 기준으로 진짜 유효한 값만 보기
#         valid_nums = [val for val, i in minq if i in v]
#         print(f"실제 남은 값: {valid_nums}\n")
        
    min_num = 0
    max_num = 0
        

        
    while minq:
        num, i = hf.heappop(minq)
        if i in v:
            min_num = num
            break

    while maxq:
        num, i = hf.heappop(maxq)
        if i in v:
            max_num = -num
            break
                
    return [max_num, min_num]
