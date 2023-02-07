file1 = list(open("data.txt").read())
for item in file1:
    if item=='F':
        print("move back")
    if item=='U':
        print("move down")
    if item=='D':
        print("move up")
    if item=='R':
        print("move left")
    if item=='L':
        print("move right")
    