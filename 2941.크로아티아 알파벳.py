word = input()
c=['c=','c-','dz=','d-','lj','nj','s=','z=']
cnt = 0
for i in c:
    cnt += word.count(i)
print(len(word)-cnt)
