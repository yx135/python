list=input()
upper=0
lower=0
print(list)
for i in list:
    print(i)
    if 'A'<=i and i<='Z':
        upper+=1
    if 'a'<=i and i<='z':
        lower+=1
print('UPPER CASE {}'.format(upper))
print('LOWER CASE {}'.format(lower))



