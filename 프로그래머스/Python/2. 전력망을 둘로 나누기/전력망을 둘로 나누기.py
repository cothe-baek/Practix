def solution(N, wires):
    from collections import deque
    answer = N
    
    """
    1. 2개로 나눠지는 간선 끊기
        - 그런 간선밖에 없는지 or 하나씩 끊어보면 확인해야 하는지
    
    2. 나눠진 거 확인은 bfs로 해야 하는지
    
    3. 트리 형태라고 하면 보통 cycle을 얘기하는 건 아닌가?
        - 찾아보니 아니네용 그러면 뭘 끊던 하나만 끊으면 2개로 나뉘긴 하겠네
        
    4. 그럼 나눠졌는지 확인은 우째 하면 될까잉
        - 사실 트리를 타고 올라가나 bfs를 하나 둘 다 똑같긴 하지
        - 그치만 어차피 트리형태이므로 dfs로 한번 해봅시다
        - 근데 dfs로 할거면 글로벌 해야 하잖어 아 몰라 그냥 dfs로 해
    """
    cnt = 1
    def count_node(i):
        cnt = 1
        q = deque()
        v = [0]*(N+1)
        
        q.append(i)
        v[i] = 1
        
        while q:
            ci = q.popleft()
            
            for ni in edge[ci]:
                if not v[ni]:
                    q.append(ni)
                    v[ni] = 1
                    cnt += 1
        
        return cnt
    
    edge = [set() for _ in range(N+1)]
    v = [0]*(N+1)
    
    for i, j in wires:
        edge[i].add(j)
        edge[j].add(i)
    
    
    for i, j in wires:
        edge[i].remove(j)
        edge[j].remove(i)
        
        cnt = count_node(i)
        answer = min(answer, abs(N - 2*cnt))
        edge[i].add(j)
        edge[j].add(i)
        
    
    
    return answer