from collections import deque
dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
def myp(arr):
    for row in arr:
        for val in row:
            print(val, end=' ')
        print()
    print()
    
def get_segments(arr, val):
    N, M = len(arr), len(arr[0])
    q = deque()
    v = [[0]*M for _ in range(N)]
    segments = []
    for i in range(N):
        for j in range(M):
            if v[i][j] or arr[i][j] != val:
                continue

            segment = [(0, 0)]

            q.append((i, j))
            v[i][j] = 1

            while q:
                ci, cj = q.popleft()

                for di, dj in dirs:
                    ni, nj = ci+di, cj+dj

                    if 0<=ni<N and 0<=nj<M and arr[ni][nj] == val and not v[ni][nj]:
                        q.append((ni, nj))
                        v[ni][nj] = 1
                        segment.append((ni-i, nj-j))
                
            segments.append(segment)
    
    return segments

def organize_segment(segment):
    new_seg = []
    mxi, mxj = -51, -51
    mni, mnj = 51, 51
    
    for (i, j) in segment:
        mxi, mxj = max(mxi, i), max(mxj, j)
        mni, mnj = min(mni, i), min(mnj, j)        
    
    # print(mxi, mxj, mni, mnj)
    mxi -= mni
    mxj -= mnj
    # print(mxi, mxj)
    
    for s in range(len(segment)):
        i, j = segment[s]
        segment[s] = (i-mni, j-mnj)
    
    new_seg.append(sorted(segment[:]))
    
    mx = max(mxi, mxj)
    
    for _ in range(3):
        nseg = []
        mni, mnj = 51, 51
        for (i, j) in segment:
            ni, nj = j, mx-i
            nseg.append((ni, nj))
            mni = min(mni, ni)
            mnj = min(mnj, nj)
        
        for s in range(len(nseg)):
            i, j = nseg[s]
            nseg[s] = (i-mni, j-mnj)
        
        segment = sorted(nseg[:])
        new_seg.append(segment)
    
    return new_seg

def solution(game_board, table):
    N, M = len(table), len(table[0])
    
    segments = get_segments(table, 1)
    
    # puzzles: i번째 조각의 j개 회전 버전
    puzzles = []
    for segment in segments:
        new_seg = organize_segment(segment)
        puzzles.append(new_seg)
    
    vacancies = get_segments(game_board, 0)
    spaces = []
    for space in vacancies:
        mni = min([x for (x, y) in space])
        mnj = min([y for (x, y) in space])
        space = [(i-mni, j-mnj) for (i, j) in space]
        space.sort()
        spaces.append(space)
        
    # i번째 퍼즐로 빈칸 채우기
    v = [0] * len(puzzles)
    answer = 0
    for space in spaces:
        for idx, puzzle in enumerate(puzzles):
            if v[idx] or len(puzzle[0]) != len(space):
                continue
            
            if space in puzzle:
                v[idx] = 1
                answer += len(space)
                break
        
    return answer