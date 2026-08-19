

def solution(arr):
    """
    이게 왜 dp야 -> 연산 순서만 바뀌니까
    
    mn[i][j]: i번째 숫자부터 j번째 숫자까지 계산했을 때 최솟값
    mx[i][j]: i번째 숫자부터 j번째 숫자까지 계산했을 때 최댓값
    
    그럼 값 업데이트를 일단 2개씩 묶어서 먼저 계산하고 그담 3개 그담 4개 이렇게 하면 되나
    일단 인덱스 헷갈리니까 문자랑 숫자랑 나눠야 하나
    """
    nlst = [int(arr[0])]
    olst = []
    
    for i in range(1, len(arr), 2):
        nlst.append(int(arr[i+1]))
        olst.append(arr[i])
    N = len(nlst)
    INF = float('inf')
    
    mn = [[INF]*N for _ in range(N)]
    mx = [[-INF]*N for _ in range(N)]
    
    print(nlst)
    print(olst)
    print()
    
    def myp(arr):
        for row in arr:
            for val in row:
                if val == INF or val == -INF:
                    print(f'[]', end=' ')
                else:
                    print(f'{val:>2}', end=' ')
            print()
        print()
    
    for i in range(len(nlst)):
        mn[i][i] = nlst[i]
        mx[i][i] = nlst[i]
    
    # k = 1
    # for i in range(len(nlst) - k):
    #     j = i + k
    #     if olst[i] == '+':
    #         mn[i][j] = min(mn[i][j], nlst[i] + nlst[j])
    #         mx[i][j] = max(mx[i][j], nlst[i] + nlst[j])
    #     elif olst[i] == '-':
    #         large = max(nlst[i], nlst[j])
    #         small = min(nlst[i], nlst[j])
    #         mn[i][j] = min(mn[i][j], nlst[i] - nlst[j])
    #         mx[i][j] = max(mx[i][j], nlst[i] - nlst[j])
    

    
    for k in range(1, N):
        for i in range(N - k):
            j = i + k
            for n in range(i, j):
                if olst[n] == '+':
                    mn[i][j] = min(mn[i][j], mn[i][n] + mn[n+1][j])
                    mx[i][j] = max(mx[i][j], mx[i][n] + mx[n+1][j])

                elif olst[n] == '-':
                    large = max(mx[i][n] - mn[n+1][j], mn[i][n] - mx[n+1][j])
                    small = min(mx[i][n] - mn[n+1][j], mn[i][n] - mx[n+1][j])
                    mn[i][j] = min(mn[i][j], small)
                    mx[i][j] = max(mx[i][j], large)
    
    
    # myp(mn)
    # myp(mx)
    
    return mx[0][N-1]