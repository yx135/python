
dic={}
sum=0
while True:
    dic.clear()
    a=input().split()
    if a[0]=='Q':
        break
    dic[a[0]]=a[1]
    print(dic)
    if  'D' in dic:
        sum=sum+int(dic['D'])
    elif 'W' in dic:
        sum=sum-int(dic['W'])
    dic.clear()
    a.clear()
print(sum)