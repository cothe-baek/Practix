def solution(enroll, referral, seller, amount):
    from collections import deque, defaultdict
    N = len(enroll)
    
    parent = defaultdict(str)
    childs = defaultdict(list)
    profit = defaultdict(int)
    sells = defaultdict(list)
    q = []
    
    for i in range(N):
        person = enroll[i]
        ref = referral[i]
        
        if ref == '-':
            q.append(person)
            
        childs[ref].append(person)
        parent[person] = ref
    
    for i in range(len(seller)):
        person = seller[i]
        money = amount[i]*100
        sells[person].append(money)
    
    tree = [['-']]
    while q:
        nq = []
        tree.append(q[:])
        for cp in q:
            for np in childs[cp]:
                nq.append(np)
        q = nq
    
    for i in range(len(tree)-1, 0, -1):
        layer = tree[i]
        for person in layer:
            for money in sells[person]:
                pay = money // 10
                profit[person] += money - pay
                cur_person = person
                
                while pay > 0 and cur_person != '-':
                    profit[parent[cur_person]] += (pay - pay//10)
                    
                    pay //= 10
                    cur_person = parent[cur_person]
        
            # print(person, profit)
        
        
    answer = []
    for i in range(N):
        person = enroll[i]
        answer.append(profit[person])
    
    return answer