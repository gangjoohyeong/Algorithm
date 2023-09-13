from collections import deque

def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(queue1), sum(queue2)
    
    if (sum1 + sum2) % 2 != 0:
        return -1
    
    check = (sum1 + sum2) / 2
    count = 0
    maximum_count = len(queue1) + len(queue2)
    
    while sum1 != sum2:
        if count >= maximum_count:
            return -1
        
        while queue1 and sum1 > sum2:
            now = queue1.popleft()
            queue2.append(now)
            count += 1
            sum1 -= now
            sum2 += now
        
        while queue2 and sum1 < sum2:
            now = queue2.popleft()
            queue1.append(now)
            count += 1
            sum1 += now
            sum2 -= now

    return count