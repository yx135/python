a=input().split(' ')
a.sort()
print(a)
num={}
for i in a:
   num[i]=a.count(i)

for i in num:
    print('{0}:{1}').format(i,mum[i])