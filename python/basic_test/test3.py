"""
n=int(input())
dic={}
for i in range(1,n+1):
    dic[i]=i*i
print(dic)
"""
try:
    n=int(input("please input number: "))
    ans={i:i*i for i in range(1,n+1)}
    print(ans)
except ValueError as err:
    print(err)
