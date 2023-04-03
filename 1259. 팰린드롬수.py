
while 1:
    num = [int(i) for i in input()]
    if num == [0]:
        break
    elif num == list(reversed(num)):
        print("yes")
    else:
        print("no")


