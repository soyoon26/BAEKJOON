while True:
    try:
        n=int(input())
        if n == 1:
            print('1')
            break
        i='1'
        while True:
            if int(i)%n==0:
                print(len(i))
                break
            else:
                i+='1'
    except:
        break

#num = num*10 + 1