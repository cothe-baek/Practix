def solution(N, lost, reserve):
    
    student = [1] * (N+1)
    v = [0] * (N+1)
    for n in lost:
        student[n] -= 1
    for n in reserve:
        student[n] += 1
        
    cnt = 0
    # print(student)
    for i in range(1, N+1):
        if v[i]:
            continue
        if student[i] == 2:
            cnt += 1
            v[i] = 1
            if student[i-1] == 0:
                student[i] -= 1
                student[i-1] += 1
                v[i-1] = 1
                cnt += 1
            elif i <= N-1 and student[i+1] == 0:
                student[i] -= 1
                student[i+1] += 1
                v[i+1] = 1
                cnt += 1
        
        elif student[i] == 1:
            v[i] = 1
            cnt += 1
    
        # print(cnt, student)
    return cnt