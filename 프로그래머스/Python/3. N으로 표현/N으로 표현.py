def myp(arr):
    for row in arr:
        for val in row:
            print(val, end=' ')
        print()
    print()

def solution(N, number):
    answer = -1
    
    """
    arr[i][j]: i~j번째 까지로 만든 계산 결과 set
    k 루프
    k개씩만 하면서 사칙연산
    
    dp[i]: N을 i번 써서 만들 수 있는 숫자 set
    1번써서 만든 거 계산 (0/1)
    2번 써서 만든 거 계산 (0/2 1/1)
    3번 써서 만든 거 계산 (0/3 1/2)
    4번 써서 만든 거 계산 (0/4 1/3 2/2)
    """
    dp = [set() for _ in range(9)]
    
    for i in range(1, 9):
        dp[i].add(int(str(N)*i))
        
        # 지금 i값에서 나오는 조합들 탐색
        for k in range(i):
            j = i - k
            for a in dp[j]:
                for b in dp[k]:
                    dp[i].add(a + b)
                    dp[i].add(abs(a - b))
                    dp[i].add(a * b)
                    if b != 0:
                        dp[i].add(a // b)
            
    for i in range(1, 9):
        if number in dp[i]:
            answer = i
            break
    
    return answer