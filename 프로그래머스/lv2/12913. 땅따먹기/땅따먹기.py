def solution(land):
    score = [ [ 0 for _ in range(len(land[0])) ] for _ in range(len(land)) ]
    score[0] = land[0]
    for idx1, la in enumerate(land[1:]):
        for idx2, l in enumerate(la):
            score[idx1+1][idx2] = l + max(score[idx1][:idx2] + score[idx1][idx2+1:])
    return max(score[-1])