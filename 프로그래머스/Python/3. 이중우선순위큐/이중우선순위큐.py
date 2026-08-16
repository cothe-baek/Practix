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
                while True:
                    if v and minq:
                        if minq[0][1] in v:
                            num, i = hf.heappop(minq)
                            v.remove(i)
                            break
                        else:
                            hf.heappop(minq)
                    else:
                        break
                        
            
            if val == 1:
                while True:
                    if v and maxq:
                        if maxq[0][1] in v:
                            num, i = hf.heappop(maxq)
                            v.remove(i)
                            break
                        else:
                            hf.heappop(maxq)
                    else:
                        break
                    
        # print(op)
        # print(minq)
        # print(maxq)
        # print(v)
        # print()
        
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