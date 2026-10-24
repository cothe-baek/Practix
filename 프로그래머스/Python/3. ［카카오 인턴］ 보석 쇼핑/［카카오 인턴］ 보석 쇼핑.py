from collections import defaultdict, Counter
DBG = False

def solution(gems):
    answer = []
    window_cnt = Counter(gems)
    for k, v in window_cnt.items():
        window_cnt[k] = 0
    diversity = len(window_cnt)
    N = len(gems)
    
    left, right = 0, 0
    cur_diversity = 0
    mn_range = N+1
    
    while right < N or cur_diversity == diversity:
            
        if cur_diversity < diversity:
            if not window_cnt[gems[right]]:
                cur_diversity += 1
            window_cnt[gems[right]] += 1
            right += 1

        else:
            if right-left < mn_range:
                answer = [left+1, right]
                mn_range = right-left
            
            window_cnt[gems[left]] -= 1
            if not window_cnt[gems[left]]:
                cur_diversity -= 1
            left += 1
        
    return answer