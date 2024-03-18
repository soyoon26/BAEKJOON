import sys
n,k=map(int,sys.stdin.readline().split())
mails = {}
for i in range(k):
    mail=sys.stdin.readline().split()
    if mail[-1] in mails:
        if mails[mail[-1]] < len(mail):
            mails[mail[-1]] = len(mail)
    else:
        mails[mail[-1]] = len(mail)
if n>=sum(mails.values()):
    print('YES')
else:
    print('NO')