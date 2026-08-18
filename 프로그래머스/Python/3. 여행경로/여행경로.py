def solution(tickets):
    answer = []
    N = len(tickets)
    edge = {}
    
    for pos, [i, j] in enumerate(tickets):
        if i in edge:
            edge[i].append((j, pos))
        else:
            edge[i] = [(j, pos)]
        
    for i in edge:
        edge[i].sort()
        
    # print(edge)
    
    lst = ["ICN"]
    v = set()
    done = False
    
    def dfs(cur):
        nonlocal done, answer
        if done:
            return
        
        if len(lst) == N+1:
            # print('done')
            # print(lst)
            done = True
            answer = lst.copy()
            return
        
        if cur not in edge:
            return
            
        for nxt, pos in edge[cur]:
            if pos in v:
                continue
            
            v.add(pos)
            lst.append(nxt)
            
            dfs(nxt)
            
            v.remove(pos)
            lst.pop()
    
    dfs("ICN")
    
    return answer