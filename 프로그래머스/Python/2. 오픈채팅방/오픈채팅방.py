def solution(record):
    answer = []
    log = []
    users = {}
    
    for rec in record:
        got = rec.split()
        if len(got) == 2:
            cmd, uid = got[0], got[1]
        else:
            cmd, uid, nick = got[0], got[1], got[2]
            
        
        if cmd == 'Enter':
            users[uid] = nick
            log.append((uid, 'Enter'))
        
        elif cmd == 'Leave':
            log.append((uid, 'Leave'))
        
        else:
            users[uid] = nick
        
    
    for uid, cmd in log:
        if cmd == 'Enter':
            answer.append(users[uid] + "님이 들어왔습니다.")
        elif cmd == 'Leave':
            answer.append(users[uid] + "님이 나갔습니다.")
            
    return answer