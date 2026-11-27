def solution(stones, k):
    from collections import defaultdict
    answer = 0
    N = len(stones)
    stone_dict = defaultdict(list)
    
    for i, x in enumerate(stones):
        stone_dict[x].append(i+1)
    
    order = [(x, lst) for x, lst in stone_dict.items()]
    order.sort()
    
    # print(order)
        
    # 더미노드 0, N+1 / 진짜 노드 1~N
    left = [x for x in range(-1, N+1)]
    right = [x for x in range(1, N+3)]
    
    for x, lst in order:
        answer = x
        for i in lst:
            a, b = left[i], right[i]
            right[left[i]], left[right[i]] = b, a
            
            # print(f'{i}th stone broken, {a} and {b} connected')
            if b - a > k:
                return answer
        
        # print('stidx: ' + ' '.join([f'{x:>2}' for x in range(N+1)]))
        # print('left : ' + ' '.join([f'{x:>2}' for x in left]))
        # print('right: ' + ' '.join([f'{x:>2}' for x in right]))
        # print()
    
    return answer