n = 5
for i in range(n):
    print('* ' * (n - i - 1), end='')
    print(*range(1, i + 2))

for i in range(n):
    print(*range(1, n - i), end=' ')
    print('* ' * (i + 1))
