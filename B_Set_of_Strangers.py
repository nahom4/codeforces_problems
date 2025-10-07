t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    matrix = []
    mx_value = float("-inf")
    for _ in range(n):
        row = list(map(int,input().split()))
        mx_value = max(mx_value,max(row))
        matrix.append(row)


    non_stranger = [0] * (mx_value + 1)
    colors = [0] * (mx_value + 1)
    direction = [(1,0),(-1,0),(0,1),(0,-1)]

    def is_valid(r,c):
        if 0 <= r < n and 0 <= c < m:
            return True
        return False
    for i in range(n):
        for j in range(m):
            for x,y in direction:
                if is_valid(i + x,j + y):
                    if matrix[i][j] == matrix[i + x][j + y]:
                        non_stranger[matrix[i][j]] = 1

                colors[matrix[i][j]] = 1

    # strangers = len(colors) - len(non_stranger)
    no_colors = colors.count(1)
    no_non_stranger = non_stranger.count(1)
    strangers = no_colors - no_non_stranger


    if no_non_stranger:
        print(strangers + (no_non_stranger - 1) * 2)

    else:
        print(strangers - 1)

