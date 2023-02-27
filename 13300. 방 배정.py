N, K = map(int,input().split())
girl = []
boy = []
for i in range(N):
    gender, grade = map(int,input().split())
    if gender == 0:
        girl.append(grade)
    else :
        boy.append(grade)


room_cnt = 0
#여학생
for i in range(1,7): #6학년까지
    cnt = 0
    for j in girl:
        if i == j:
            cnt += 1
    if cnt > K : #학생수가 방 최대수용인원보다 크면
        room_cnt += room_cnt//K
        if room_cnt % K:
            room_cnt += 1
    elif K >= cnt > 0:   #학생수가 방 하나에 다 들어가면
        room_cnt += 1
#남학생
for i in range(1,7): #6학년까지
    cnt = 0
    for j in boy:
        if i == j:
            cnt += 1
    if cnt > K : #학생수가 방 최대수용인원보다 크면
        if room_cnt % K:
            room_cnt += 1
        room_cnt += cnt // K
    elif K >= cnt > 0:   #학생수가 방 하나에 다 들어가면
        room_cnt += 1

print(room_cnt)




