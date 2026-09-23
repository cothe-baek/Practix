def bisect_left(lst, num):
    
    lo, hi = 0, len(lst)
    
    while lo < hi:
        mid = (lo + hi) // 2
        
        if lst[mid] < num:
            lo = mid + 1
        else:
            hi = mid
    
    return lo
    

def solution(infos, queries):
    answer = []
    lang = ['cpp', 'java', 'python', '-']
    task = ['backend', 'frontend', '-']
    hist = ['junior', 'senior', '-']
    food = ['chicken', 'pizza', '-']

    info_lst = [lang, task, hist, food]
    comb = []
    tmp = []
    def dfs(depth):
        if depth == 4:
            comb.append(tmp[:])
            return
    
        for i in range(len(info_lst[depth])):
            tmp.append(info_lst[depth][i])
            dfs(depth+1)
            tmp.pop()
    
    dfs(0)
    
    info_dict = {}
    for k in comb:
        info_dict[tuple(k)] = []
        
    for i, info in enumerate(infos):
        lst = list(info.split())
        score = int(lst[-1])
        
        for a in ((lst[0], '-')):
            for b in ((lst[1], '-')):
                for c in ((lst[2], '-')):
                    for d in ((lst[3], '-')):
                        info_dict[(a, b, c, d)].append(score)
    
    for k, v in info_dict.items():
        v.sort()
        # print(v)
    
    for query in queries:
        a, _, b, _, c, _, d, score = query.split()
        score = int(score)
        
        idx = bisect_left(info_dict[(a, b, c, d)], score)
        answer.append(len(info_dict[(a, b, c, d)]) - idx)
        
    return answer