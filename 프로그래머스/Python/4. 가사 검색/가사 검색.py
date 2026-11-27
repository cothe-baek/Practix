def solution(words, queries):
    from collections import defaultdict
    answer = []
    
    # key: 단어 val: child list
    forward = defaultdict(dict)
    backward = defaultdict(dict)
    total_cnt = defaultdict(int)
    
    for word in words:
        tmp = forward[len(word)]
        total_cnt[len(word)] += 1
        
        for c in word:
            if c not in tmp:
                tmp[c] = {'cnt': 0}
                
            tmp[c]['cnt'] += 1
            tmp = tmp[c]
        
        tmp = backward[len(word)]
        for c in word[::-1]:
            if c not in tmp:
                tmp[c] = {'cnt': 0}
                
            tmp[c]['cnt'] += 1
            tmp = tmp[c]
    
    for query in queries:
        if len(query) not in forward:
            answer.append(0)
            continue
        
        if query[-1] == '?' and query[0] == '?':
            answer.append(total_cnt[len(query)])
            
        elif query[-1] == '?':
            tmp = forward[len(query)]
            for c in query:
                if c == '?':
                    answer.append(tmp['cnt'])
                    break
                if c in tmp:
                    tmp = tmp[c]
                else:
                    answer.append(0)
                    break
            else:
                answer.append(tmp['cnt'])
        
        else:
            tmp = backward[len(query)]
            for c in query[::-1]:
                if c == '?':
                    answer.append(tmp['cnt'])
                    break
                if c in tmp:
                    tmp = tmp[c]
                else:
                    answer.append(0)
                    break
            else:
                answer.append(tmp['cnt'])
        
    return answer