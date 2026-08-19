from collections import deque
from collections import defaultdict

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
    
    for _ in range(4):
        mni, mnj = 51, 51
        for (i, j) in segment:
            mni = min(mni, -i)
            mnj = min(mnj, j)
        
        segment = [(j-mnj, -i-mni) for i, j in segment]
        new_seg.append(tuple(sorted(segment)))
        
    return new_seg

def organize_space(space):
    new_seg = []
    
    mni, mnj = 51, 51
    for (i, j) in space:
        mni = min(mni, i)
        mnj = min(mnj, j)

    space = [(i-mni, j-mnj) for i, j in space]
    
    return tuple(sorted(space))

def solution(game_board, table):
    answer = -1
    N, M = len(table), len(table[0])
    
    segments = get_segments(table, 1)
    puzzles = []
    for segment in segments:
        new_seg = organize_segment(segment)
        puzzles.append(new_seg)
    
    empty = get_segments(game_board, 0)
    
    spaces = defaultdict(int)
    
    for idx, space in enumerate(empty):
        space = organize_space(space)
        spaces[tuple(space)] += 1
    
    cnt = 0
    for puzzle in puzzles:
        done = False
        for seg in puzzle:
            if done:
                continue
            
            if seg in spaces and spaces[seg]:
                spaces[seg] -= 1
                cnt += len(seg)
                break
        
        
    return cnt