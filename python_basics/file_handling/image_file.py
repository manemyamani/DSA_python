f=open('profile.jpg','rb')
f1=open('profile1.jpg','wb')
for i in f:
    f1.write(i)