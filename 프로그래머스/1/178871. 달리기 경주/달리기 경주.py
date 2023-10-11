def solution(players, callings):
    players_dict = { val : idx for idx, val in enumerate(players) }
    for calling in callings:
        idx = players_dict[calling] 
        players_dict[calling] -= 1
        players_dict[players[idx-1]] += 1
        players[idx-1], players[idx] = players[idx], players[idx-1]
    return players