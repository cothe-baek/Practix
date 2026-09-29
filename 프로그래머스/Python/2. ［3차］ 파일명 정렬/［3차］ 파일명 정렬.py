def solution(files):
    answer = []
    lst = []
    for file in files:
        head, number, tail = "", "", ""
        i = 0
        while not file[i].isdecimal():
            head += file[i]
            i += 1
        
        while i < len(file) and file[i].isdecimal():
            number += file[i]
            i += 1
        
        if i < len(file):
            tail += file[i:]
        
        lst.append((head, number, tail))
    
    lst.sort(key = lambda x: (x[0].upper(), int(x[1])))
    
    for head, number, tail in lst:
        answer.append(head+number+tail)
            
    return answer