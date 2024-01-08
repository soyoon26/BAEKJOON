word = list(input())
# answer = 0
# for i in word:
#     if i in ['A','B','C']:
#         answer += 3
#     elif i in ['D','E','F']:
#         answer += 4
#     elif i in ['G','H','I']:
#         answer += 5
#     elif i in ['J','K','L']:
#         answer += 6
#     elif i in ['M','N','O']:
#         answer += 7
#     elif i in ['P','Q','R','S']:
#         answer += 8
#     elif i in ['T','U','V']:
#         answer += 9
#     elif i in ['W','X','Y','Z']:
#         answer += 10
#     # print(f"{i}: {answer}")
#
# print(answer)

words = {3:['A','B','C'],
    4:['D','E','F'],
    5:['G','H','I'],6:['J','K','L'],
    7:['M','N','O'],8:['P','Q','R','S'],
    9:['T','U','V'],10:['W','X','Y','Z']}

answer = 0
for i in word:
    for key,value in words.items():
        if i in value:
            answer += key
print(answer)

#딕셔너리,itmes() 사용