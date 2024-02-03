T=int(input())
for t in range(T):
    s_lst=input()
    while True:
        try:
            _,_,sound=input().split()
            s_lst=s_lst.replace(' '+sound,'')
            s_lst=s_lst.replace(sound+' ','')
        except:
            break
    print(s_lst)
#sound = a.split("goes")[1].strip() 