a = int(input())
for i in range(0, a, 1):
    for j in range(0, a-1, 1):
        print(" ", end="")
    for k in range(0, i+1, 1):
        print("*", end="")
    a -= 1
    print()
