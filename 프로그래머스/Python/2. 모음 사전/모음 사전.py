def solution(word):
    answer = 0
    chrs = ['A', 'E', 'I', 'O', 'U']
    
    cnt = 0
    def dfs(string):
        nonlocal answer, cnt
        
        if len(string) == 6 or answer:
            return
        
        if string == word:
            answer = cnt
            return
        
        cnt += 1
        for i in range(5):
            dfs(string + chrs[i])
    
    dfs('')
    
    return answer