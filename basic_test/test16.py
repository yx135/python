
list=[str(int(i)**2) for i in input().split(',') if int(i)%2!=0]
print(','.join(list))