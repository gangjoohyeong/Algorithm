def solution(babbling):
    new = []
    answer = 0
    for b in babbling:
        new.append(b.replace('aya', 'A').replace('ye', 'B').replace('woo', 'C').replace('ma', 'D'))
    for n in new:
        if n.isupper():
            stack = ['First']
            for m in n:
                if stack[-1] != m:
                    stack.append(m)
            if len(stack)-1 == len(n):
                answer += 1
    return answer