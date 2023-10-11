def solution(park, routes):
    n, m = len(park), len(park[0])
    
    for idx, val in enumerate(park):
        if 'S' in val:
            x, y = idx, val.index('S')
            break
    for route in routes:
        print(x, y)
        direction, distance = route[0], int(route[-1])
        if direction == 'E' and y + distance < m:
            for i in range(distance):
                if park[x][y+i+1] == 'X':
                    y -= distance
                    break
            y += distance
        elif direction == 'W' and y - distance >= 0:
            for i in range(distance):
                if park[x][y-i-1] == 'X':
                    y += distance
                    break
            y -= distance
        elif direction == 'S' and x + distance < n:
            for i in range(distance):
                if park[x+i+1][y] == 'X':
                    x -= distance
                    break
            x += distance
        elif direction == 'N' and x - distance >= 0:
            for i in range(distance):
                if park[x-i-1][y] == 'X':
                    x += distance
                    break
            x -= distance
            
    return [x, y]