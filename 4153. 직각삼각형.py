while 1:
    t_lst = [int(i) for i in input().split()]
    if t_lst.count(0) == 3:
        break
    else:
        t_lst.sort()
        if t_lst[0]**2 + t_lst[1]**2 == t_lst[2]**2:
            print("right")
        else :
            print("wrong")