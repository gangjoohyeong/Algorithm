def solution(numbers):
    stack = []
    answer = [ -1 for _ in range(len(numbers)) ]
    
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            # 앞 원소를 이미 stack에 담아놓은 상태에서 현재 원소와 비교 후 앞 원소를 처리
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    return answer