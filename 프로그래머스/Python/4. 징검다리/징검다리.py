def solution(distance, rocks, n):
    answer = 0
    N = len(rocks)
    rocks.sort()
    rocks.append(distance)
    
    def can_do(mid):
        pos, cnt = 0, 0
        for rock in rocks:
            if rock < pos + mid:
                cnt += 1
            else:
                pos = rock
        
        return cnt <= n
            
    # 무조건 되는 값, 무조건 안되는 값..?
    left, right = 0, distance
    
    while left < right:
        mid = (left + right + 1) // 2
        
        if can_do(mid):
            left = mid
        else:
            right = mid - 1
    
    return left