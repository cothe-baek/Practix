from collections import defaultdict, Counter
DBG = False

def solution(gems):
    answer = []
    diversity = len(Counter(gems))   # 이거 문제에서 요구하는 수치라는 걸 나타낼 수 있는 변수명 없을까
    N = len(gems)
    
    """
    모든 종류 보석을 포함하는 가장 짧은 구간 찾기
    아 분명히 풀어봤는데
    왜 기억이 안날까
    투포인터 문제인가
    첨에 0, 0으로 놓고
    diversity 만족 못하면 right 증가
    만족하면 현재 구간 기록하고 left 증가
    right < left 면 종료
    right가 N-1인데 diversity 만족 못하면 종료
    """
    
    left, right = 0, 0
    cur_diversity = 1
    cur_gems = defaultdict(int) # cur_gems도 변수명 맘에 안듦
    cur_gems[gems[0]] += 1
    mn_range = 100001
    
    while left < right or right < N:
        if DBG:
            print(left, right, cur_diversity)
            for k, v in cur_gems.items():
                print(k, v)
            print()
            
        if cur_diversity < diversity:
            if right == N-1:
                break
            right += 1
            if cur_gems[gems[right]] == 0:
                cur_diversity += 1
            cur_gems[gems[right]] += 1
            # defaultdict니까 이렇게 하면 새로운 key 생기지만 개수로 할거라 상관 x
            # 없을 때만 더하기

            
        else:   # 이상일 수는 없음 무조건 같음
            if right-left+1 < mn_range:
                answer = [left+1, right+1]
                mn_range = right-left+1
            
            if left + 1 > right:
                right += 1
            else:
                assert cur_gems[gems[left]], print('ERR')
                cur_gems[gems[left]] -= 1
                if cur_gems[gems[left]] == 0:
                    cur_diversity -= 1
                left += 1
        
    return answer