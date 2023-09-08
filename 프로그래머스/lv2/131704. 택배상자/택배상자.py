def solution(order):
    answer = 0
    now = 1
    length = len(order)
    array = []
    for o in order:
        # 초기 순서에서 다 꺼냈을 때
        if now > length:
            tmp = array.pop()
            if tmp != o:
                return answer
            else:
                answer += 1
                continue
        # 아직 남았을 때
        else:
            while True:
                if now > length:
                    break
                if now == o:
                    now += 1
                    answer += 1
                    break
                else:
                    if array and array[-1] == o:
                        array.pop()
                        answer += 1
                        break
                    array.append(now)
                    now += 1
                    continue
    return answer


[1,2,3]