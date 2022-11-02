def solution(a):
    
    store = {}
    
    for num in a:
        if num not in store:
            store[num] = 1
        else:
            return num
            
    return -1
