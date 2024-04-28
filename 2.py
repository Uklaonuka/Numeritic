size = input()
m = int(size[0])
n = int(size[2])
matrix = []
i = 0
while i < m:
    a = input()
    a = a.split()
    a = [int(c) for c in a]
    matrix.append(a)
    i += 1
matrix = [[matrix[i][j] for i in range(m)] for j in range(n)]
i = 0
while i < n:
    a = (matrix[i][::-1])
    a = ' '.join(map(str, a))
    print(a)
    i += 1

