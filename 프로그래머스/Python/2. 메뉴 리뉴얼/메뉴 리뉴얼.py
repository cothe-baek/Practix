from collections import defaultdict
def solution(orders, course):
    answer = []
    course_set = set(course)
    mx_course = max(course)
    candis = defaultdict(int)
    
    """
    이전에 손님들이 가장 많이 함께 주문한 단품 메뉴들을 코스요리 메뉴로 구성하기
        - 최소 2가지 이상의 단품 메뉴로 구성
        - 최소 2명 이상의 손님이 주문한 조합
        - 근데 만드는 코스요리 메뉴의 코스 길이는 정해져 있음
        - 같은 길이의 코스중엔 제일 cnt 많은 것만, 여러개면 모두
    
    1. 손님 주문 오름차순 sort하고 원하는 길이의 모든 조합 생성하기
    2. 손님 단위로 v 초기화 하면서 dict에서 count
    3. 조건 만족하는 거 한군데 모으고 sort
    """
    
    def dfs(tmp, n):
        if len(tmp) > mx_course:
            return
            
        if len(tmp) in course_set:
            candis[tmp] += 1
            
        for i in range(n, len(order)):
            dfs(tmp + order[i], i+1)
    
    for order in orders:
        order = sorted(list(order))
        dfs("", 0)
    
    mx_cnt = [0] * (mx_course+1)
    menu = {}
    
    for k, v in candis.items():
        if v >= 2:
            if v > mx_cnt[len(k)]:
                menu[len(k)] = [k]
                mx_cnt[len(k)] = v
            elif v == mx_cnt[len(k)]:
                menu[len(k)].append(k)
    
    for k, v in menu.items():
        answer += v
    
    answer.sort()
    
    return answer