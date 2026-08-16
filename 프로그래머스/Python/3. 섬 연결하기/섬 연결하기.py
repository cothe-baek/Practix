def solution(N, costs):
    answer = 0
    """
    1. 연결하는 기준
    2. 다 이어졌는지 어떻게 판별하는지
    
    싼거부터 연결하면서, root 노드를 비교해서 이어졌는지 판별
    싸이클이 생기지 않게끔 하면서 연결이 끝나면 끝!
    """
    
    costs.sort(key = lambda x: x[2])
    root = [x for x in range(N)]
    
    cnt = 0
    
    def find_root(x):
        if root[x] != x:
            root[x] = find_root(root[x])
            
        return root[x]
    
    def merge(x, y):
        
        a = find_root(x)
        b = find_root(y)
        
        if a < b:
            root[b] = a
        else:
            root[a] = b
    
    for i, j, cost in costs:
        # root 노드가 같으면 이미 같은 그룹이란 얘기, 스킵
        if find_root(i) == find_root(j):
            continue
        
        # 다르다면 연결
        merge(i, j)
        answer += cost
        cnt += 1
        
        if cnt == N-1:
            break
        
    return answer