def solution(n, lost, reserve):
    diff_lost = list(set(lost) - set(reserve))
    diff_reserve = list(set(reserve) - set(lost))

    for r in diff_reserve:
        if r-1 in diff_lost:
            diff_lost.remove(r-1)
            continue
        elif r+1 in diff_lost:
            diff_lost.remove(r+1)
    return n - len(diff_lost)