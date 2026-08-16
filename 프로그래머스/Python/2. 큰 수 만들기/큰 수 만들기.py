def solution(number, k):
    answer = ''
    N = len(number)
    """
    [new]
    k를 숫자 스킵 티켓이라고 생각하고
    어차피 제일 높은 자리수가 높은 게 중요하니
    하나씩 보면서 최대 k개 까지 스킵하되, 그 중에 제일 높은 걸 선택하기
    
    [+]
    선택 끝난 후에 k가 남아있으면 그만큼 뒤에서부터 삭제
    """
    for i in range(N):
        if not answer:
            answer += number[i]
        else:
            while answer and answer[-1] < number[i] and k:
                answer = answer[:-1]
                k -= 1
            answer += number[i]
    
    while k:
        answer = answer[:-1]
        k -= 1
    
    return answer