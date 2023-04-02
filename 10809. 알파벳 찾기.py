from string import ascii_lowercase
alph_list = list(ascii_lowercase)
str = input()
for i in alph_list:
    if i in str:
        print(str.index(i), end = " ")
    else:
        print("-1",end = " ")
