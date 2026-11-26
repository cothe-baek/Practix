def solution(n, k, cmd):
    DBG = False
    
    prv = [x for x in range(n)]
    nxt = [x for x in range(n)]
    alive = [True for _ in range(n)]
    stack = []
    cur_node = k
    
    for i in range(n):
        if i > 0:
            prv[i] = i-1
        if i < n-1:
            nxt[i] = i+1
    
    if DBG:
        print('cur_node:', cur_node)
        print(prv)
        print(nxt)
        
    for c in cmd:
        q, *x = c.split()
        
        if q == 'U':
            for x in range(int(x[0])):
                cur_node = prv[cur_node]
        
        elif q == 'D':
            for x in range(int(x[0])):
                cur_node = nxt[cur_node]
            
        elif q == 'C':
            prv_node, nxt_node = prv[cur_node], nxt[cur_node]
            
            if prv_node != cur_node:
                if nxt[prv_node] == nxt_node:
                    nxt[prv_node] = prv_node
                else:
                    nxt[prv_node] = nxt_node
            
            if nxt_node != cur_node:
                if prv[nxt_node] == prv_node:
                    prv[nxt_node] = nxt_node
                else:
                    prv[nxt_node] = prv_node
            
            stack.append(cur_node)
            alive[cur_node] = False
            
            if nxt[cur_node] == cur_node:
                cur_node = prv_node
            else:
                cur_node = nxt_node
        
        else:
            new_node = stack.pop()
            alive[new_node] = True
            
            if nxt[new_node] != new_node:
                prv[nxt[new_node]] = new_node
            
            if prv[new_node] != new_node:
                nxt[prv[new_node]] = new_node
        
        if DBG:
            print(c, 'cur_node:', cur_node)
            print(prv)
            print(nxt)
            print()
    
    answer = ''.join('O' if alive[i] else 'X' for i in range(n))
    if DBG: print(answer)
    return answer