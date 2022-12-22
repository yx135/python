"""
for i in range(2000,3200):
    if i%7==0 and i%5!=0:
        print(i,end=',')
    else:
        pass     
"""
print([x for x in range(2000,3021) if x%7==0 and x%5 !=0])