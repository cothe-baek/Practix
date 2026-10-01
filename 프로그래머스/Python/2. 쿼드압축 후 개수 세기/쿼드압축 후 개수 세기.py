def solution(arr):
    answer = [0, 0]
    N = len(arr)
        
    def compress(si, sj, ei, ej):
        
        # print(f'from {si, sj} to {ei, ej}')
        
        num = arr[si][sj]
        
#         narr = [row[sj:ej] for row  in arr[si:ei]]
#         # for row in narr:
#         #     for val in row:
#         #         print(val, end=' ')
#         #     print()
#         # print()
        
#         total =  sum(sum(row) for row in narr)
        
        
#         if total == (ei-si) * (ej-sj) or total == 0:
#             answer[num] += 1
#         else:
#             di, dj = (si + ei) // 2, (sj + ej) // 2
#             compress(si, sj, di, dj, depth + 1)
#             compress(di, dj, ei, ej, depth + 1)
#             compress(si, dj, di, ej, depth + 1)
#             compress(di, sj, ei, dj, depth + 1)

        # version 1: 제공된 예제는 맞았지만, 실제 테스트 케이스에서 모두 실패 (시간초과도 났음)
        for i in range(si, ei):
            for j in range(sj, ej):
                if arr[i][j] != num:
                    di, dj = (si + ei) // 2, (sj + ej) // 2
                    compress(si, sj, di, dj)
                    compress(di, dj, ei, ej)
                    compress(si, dj, di, ej)
                    compress(di, sj, ei, dj)

                    return

        answer[num] += 1

    compress(0, 0, N, N)
    
    return answer