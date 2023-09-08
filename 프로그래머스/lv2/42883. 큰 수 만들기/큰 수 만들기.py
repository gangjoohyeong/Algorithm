def solution(number, k):
    stack = []
    for num in number:
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
    if k == 0:
        return ''.join(stack)
    else:
        return  ''.join(stack[:-k])