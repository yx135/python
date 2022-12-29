str=list(input())
str.sort()
print(str)
num={}
for i in str:
    num[i]=str.count(i)
print(num)