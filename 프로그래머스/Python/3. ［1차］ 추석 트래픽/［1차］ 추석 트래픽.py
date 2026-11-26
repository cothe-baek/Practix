def solution(lines):
    def str2ms(time):
        h, m, s_ms = time.split(':')
        s, ms = s_ms.split('.')
        
        h2ms = int(h) * 3600 * 1000
        m2ms = int(m) * 60 * 1000
        s2ms = int(s) * 1000
        ms = int(ms)
        
        return h2ms + m2ms + s2ms + ms
        
    
    answer = 0
    logs = []
    for line in lines:
        _, end_str, dur_str = line.split()
        
        dur_s = float(dur_str[:-1])
        dur_ms = int(dur_s * 1000)
        
        end_ms = str2ms(end_str)
        start_ms = end_ms - dur_ms + 1
        
        logs.append((start_ms, end_ms))
    
    # for log in logs:
    #     print(log)
    
    for _, start in logs:
        end = start + 999
        cnt = 0
        # print(f'from {start} to {end}')
        for start_ms, end_ms in logs:
            # print(f'start: {start_ms} / end: {end_ms}')
            if end >= end_ms >= start or start <= start_ms <= end or (start_ms <= start and end <= end_ms):
                cnt += 1
        # print(cnt)
        answer = max(answer, cnt)
    
        
    return answer