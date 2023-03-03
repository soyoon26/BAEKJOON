paper_w, paper_h = map(int,input().split())
N = int(input())

w_lst = [paper_w]  #가로 길이 리스트
h_lst = [paper_h]
for i in range(N):
    di, num = map(int,input().split())
    if di == 1:
        w_lst.append(num)
        w_lst = sorted(w_lst)  #길이 처음부터 순서대로
    else:
        h_lst.append(num)
        h_lst = sorted(h_lst)

ww_lst = [] #잘린 종이들이 들어갈 리스트
hh_lst = []
for i in w_lst[::-1]:
    ww_lst.append(paper_w - i)
    paper_w = i
    if i == w_lst[0]:
        ww_lst.append(i)

for i in h_lst[::-1]:
    hh_lst.append(paper_h - i)
    paper_h = i
    if i == h_lst[0]:
        hh_lst.append(i)

max_paper = 0

for i in hh_lst:
    for j in ww_lst:
        if max_paper < i*j:
            max_paper = i*j
print(max_paper)