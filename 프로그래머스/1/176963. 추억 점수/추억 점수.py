def solution(name, yearning, photo):
    answer = []
    
    for people in photo:
        result = 0
        for person in people:
            if person in name:
                result += yearning[name.index(person)]
        answer.append(result)
    return answer