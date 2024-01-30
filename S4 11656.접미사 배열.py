word = input()
word_lst=[]
for i in range(len(word)):
    word_lst.append(word[i:])
word_lst.sort()
print(*word_lst,sep='\n')
