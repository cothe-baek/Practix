def solve(commands):
    DBG = False
    answer = []
    N = 50
    groups = [[set([(i, j)]) for j in range(N)] for i in range(N)]
    
    class cell:
        def __init__(self, r, c, val):
            self.r = r
            self.c = c
            self.val = val
            self.merged = False
            self.parent = (r, c)
        
        @property
        def prt(self):
            return f'{self.val}'
    
    arr = [[cell(i, j, None) for j in range(N)] for i in range(N)]
    
    # for i in range(N):
    #     for j in range(N):
    #         print(arr[i][j].prt, end=' ')
    #     print()
    
    for cmd in commands:
        q = list(cmd.split())
        
        if q[0] == 'UPDATE' and len(q) == 4:
            r, c, val = q[1:]
            r, c = int(r)-1, int(c)-1
            pr, pc = arr[r][c].parent
            
            for i, j in groups[pr][pc]:
                arr[i][j].val = val
        
        elif q[0] == 'UPDATE' and len(q) == 3:
            val1, val2 = q[1:]
            # 2500 * 1000 = 250만, 굳이 hash 필요 x
            for i in range(N):
                for j in range(N):
                    if arr[i][j].val == val1:
                        arr[i][j].val = val2
        
        elif q[0] == 'MERGE':
            r1, c1, r2, c2 = (int(v)-1 for v in q[1:])
            
            # 두 위치가 같은 셀이면 무시
            if arr[r1][c1].parent == arr[r2][c2].parent:
                continue
            
            # 병합
            pr1, pc1 = arr[r1][c1].parent
            pr2, pc2 = arr[r2][c2].parent
            
            pr, pc = min((pr1, pc1), (pr2, pc2))
            arr[r1][c1].parent = (pr, pc)
            arr[r2][c2].parent = (pr, pc)
            
            val = arr[r1][c1].val if arr[r1][c1].val is not None else arr[r2][c2].val
            
            # 굳이 이 단계에서 groups[r1][c1] 초기화할 필요는 없음. 나중에 병합 해제할 때 초기화 되니까
            groups[pr][pc].update(groups[pr1][pc1])
            groups[pr][pc].update(groups[pr2][pc2])
            
            for r, c in groups[pr][pc]:
                arr[r][c].val = val
                arr[r][c].parent = (pr, pc)
            
            if DBG: print("\n parent group:", pr, pc, groups[pr][pc])
            
            
        elif q[0] == 'UNMERGE':
            r, c = (int(v)-1 for v in q[1:])
            pr, pc = arr[r][c].parent
            if DBG: print("\n parent group:", pr, pc, groups[pr][pc])
            
            value = arr[pr][pc].val
            lst = list(groups[pr][pc])
            
            for i, j in lst:
                arr[i][j].parent = (i, j)
                arr[i][j].val = None
                groups[i][j] = set([(i, j)])
            
            arr[r][c].val = value
        
        else:
            r, c = (int(v)-1 for v in q[1:])
            if arr[r][c].prt == "None":
                answer.append("EMPTY")
            else:
                answer.append(arr[r][c].prt)
        
        if DBG:
            print("\n", cmd)

            for i in range(2):
                for j in range(2):
                    print('.'*8 if arr[i][j].prt == "None" else f'{arr[i][j].val:>8}', end=' ')
                print()
        
    return answer

import traceback

def solution(*args):
    try:
        return solve(*args)
    except Exception:
        return traceback.format_exc(limit=100).replace("\n", " / ")