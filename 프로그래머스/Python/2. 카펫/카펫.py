def solution(brown, yellow):
    
    for w in range(3, brown//2):
        h = (brown - 2*w + 4) // 2
            
        if (w-2) * (h-2) == yellow:
            return (max(w, h), min(w, h))
            
    return 0