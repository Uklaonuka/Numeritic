# a = int(input())
# i = 0
# forest = []
# while i < a:
#     b = input()
#     s = []
#     s.append(b[0])
#     s.append(b[1])
#     s.append(b[2])
#     forest.append(s)
#     i += 1
def max_mushrooms(n, forest):
    dp = [[0] * 3 for _ in range(n)]

    for j in range(3):
        if forest[0][j] == 'C':
            dp[0][j] = 1

    for i in range(1, n):
        for j in range(3):
            if forest[i][j] == 'W':
                continue

            dp[i][j] = max(
                dp[i-1][j-1] if j > 0 else 0,
                dp[i-1][j],
                dp[i-1][j+1] if j < 2 else 0
            )

            if forest[i][j] == 'C':
                dp[i][j] += 1


    return max(dp[-1])

n = int(input())
forest = []
for _ in range(n):
    row = input().strip()
    forest.append(row)


result = max_mushrooms(n, forest)
print(result)