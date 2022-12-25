lst=[]
while True:
    line=input()
    if len(line)==0:
        break
    lst.append(line.upper())

for line in lst:
    print(line)