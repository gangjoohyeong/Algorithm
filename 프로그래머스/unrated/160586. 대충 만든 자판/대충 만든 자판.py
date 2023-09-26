def solution(keymap, targets):
    answer = []
    for target in targets:
        target_tmp = 0
        for val in target:
            check = 0
            tmp = 101
            for key in keymap:
                if val in key:
                    tmp = min(tmp, key.index(val))
                    check = 1
            if check == 0:
                target_tmp = -1
                break
            else:
                target_tmp += tmp + 1
        answer.append(target_tmp)
    return answer