from collections import deque

def solution(n, m, section):
    answer = 0
    section = deque(section)
    while section:
        now = section.popleft()
        answer += 1
        if not section:
            return answer
        while section and section[0] < now + m:
            section.popleft()
    return answer