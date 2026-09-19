priors = [('*', '-', '+'), ('*', '+', '-'), ('-', '+', '*'), ('+', '-', '*'), ('+', '*', '-'), ('-', '*', '+')]

def merge(nums, ops, op):
    new_nums = [nums[0]]
    new_ops = [' ']
    
    for i in range(1, len(nums)):
        if ops[i] == op:
            if op == "+":
                new_num = new_nums.pop() + nums[i]
            elif op == "-":
                new_num = new_nums.pop() - nums[i]
            elif op == "*":
                new_num = new_nums.pop() * nums[i]
            new_nums.append(new_num)
        else:
            new_nums.append(nums[i])
            new_ops.append(ops[i])
        # print(new_nums)
        # print(new_ops)
    
    return new_nums, new_ops
                    
        
    

def solution(expression):
    ans = 0
    
    nums = []
    ops = [' ']
    ops_idx = 0
    
    tmp = ""
    for c in expression:
        if c == '-' or c == '*' or c == '+':
            ops.append(c)
            # ops_idx += 1
            nums.append(int(tmp))
            tmp = ""
        else:
            tmp += c
    
    nums.append(int(tmp))
    
    
    for prior in priors:
        tmp_nums, tmp_ops = nums[:], ops[:]
        # print('prior:', prior)
        for op in prior:
            # print(op, 'turn')
            tmp_nums, tmp_ops = merge(tmp_nums, tmp_ops, op)
        
        
        ans = max(ans, abs(tmp_nums[0]))
        # print(ans)
        # print()
    
    return ans