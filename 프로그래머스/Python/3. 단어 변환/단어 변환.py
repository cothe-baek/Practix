def solution(begin, target, words):
    answer = 100
    N = len(words)
    v = [0] * N
    
    def dfs(cur, depth):
        nonlocal target, answer
        
        if depth >= answer:
            return
        
        if cur == target:
            answer = depth
            return
        
        for i, word in enumerate(words):
            if not v[i]:
                cnt = 0
                for n in range(len(word)):
                    if cur[n] != word[n]:
                        cnt += 1
                        
                if cnt == 1:
                    v[i] = 1
                    dfs(word, depth+1)
                    v[i] = 0
    
    dfs(begin, 0)
    
    if answer == 100:
        answer = 0
    
    return answer 