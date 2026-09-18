def time2min(time):
    h = int(time[0:2])
    m = int(time[3:])
    return h*60 + m
"""
차량 별 누적 주차시간 기록하는 dictionary랑
차가 현재 주차중인지 아닌지 판단할 set은 있어야 할 듯
"""
def solution(fees, records):
    
    car_dict = {}
    car_state = set()
    car_lst = []
    ans = []
    
    prev_time = 0
    for record in records:
        time, car, action = record.split()
        cur_time = time2min(time)
        
        if car not in car_dict:
            car_dict[car] = 0
            car_lst.append(car)
        
        for present_car in car_state:
            car_dict[present_car] += cur_time - prev_time
        
        if action == 'IN':
            car_state.add(car)
        elif action == 'OUT':
            car_state.remove(car)
        
        prev_time = cur_time
        
    cur_time = 23*60 + 59
    for car in car_state:
        car_dict[car] += cur_time - prev_time
        
    car_lst.sort()
    
    for car in car_lst:
        total_time = car_dict[car]
        
        if total_time <= fees[0]:
            ans.append(fees[1])
        else:
            remaining_time = total_time-fees[0]
            additional_fee = (remaining_time + fees[2]-1) // fees[2] * fees[3]
            
            ans.append(fees[1] + additional_fee)
    
    return ans