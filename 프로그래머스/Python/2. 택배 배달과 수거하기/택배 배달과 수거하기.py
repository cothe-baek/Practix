def solution(cap, N, deliveries, pickups):
    answer = 0
    
    """
    먼곳부터 그리디로 가져오기
    deliver와 pickup이 충돌하는 상황은 없음
    그냥 둘 중에 0이 아닌 먼 곳 으로 가면서 처리하면 될 듯
    """
    
    pos = N-1
    total_deliver = sum(deliveries)
    total_pickup = sum(pickups)
    
    del_cap = 0
    dlst = []
    pick_cap = 0
    plst = []
    
    for i in range(N-1, -1, -1):
        while deliveries[i] > 0:
            if del_cap == 0:
                dlst.append(i+1)
                del_cap = cap
            
            if deliveries[i] >= del_cap:
                deliveries[i] -= del_cap
                del_cap = 0
            else:
                del_cap -= deliveries[i]
                deliveries[i] = 0
                
        while pickups[i] > 0:
            if pick_cap == 0:
                plst.append(i+1)
                pick_cap = cap
            
            if pickups[i] >= pick_cap:
                pickups[i] -= pick_cap
                pick_cap = 0
            else:
                pick_cap -= pickups[i]
                pickups[i] = 0
                
    
    # print(dlst)
    # print(plst)
    
    length = max(len(dlst), len(plst))
    
    dlst += [0] * (length-len(dlst))
    plst += [0] * (length-len(plst))
    
    for i in range(length):
        answer += max(dlst[i], plst[i]) * 2
        
    return answer