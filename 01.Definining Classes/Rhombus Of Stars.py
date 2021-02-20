star = '* '
empty = " "
n = int(input())

# start
for row in range(1, n):
    print(f"{(n - row) * empty}{row * star}")

# middle
print(f"{n * star}")

# end
for row in reversed(range(1, n)):
    print(f"{(n - row) * empty}{row * star}")