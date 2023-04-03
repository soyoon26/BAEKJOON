x, y, w, h = map(int,input().split())
lst = [x-0,y-0,abs(x-w),abs(y-h)]
print(min(lst))

