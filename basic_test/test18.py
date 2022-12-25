def a_z(s):
    strs=s
    for i in strs:
     if 'z'>=i and i>='a':
        return True
    else:
        return False
def A_Z(s):
    strs=s
    for i in strs:
     if 'Z'>=i and i>='A':
        return True
    else:
        return False

def number(s):
    strs=s
    for i in strs:
     if '0'<=i and i<='9':
        return True
    else:
        return False

def character(s):
    strs=s
    for i in strs:
     if i=='$' or i=='#' or i=='@':
        return True
    else:
        return False
def length(s):
    if 6<=len(s) and len(s)<=12:
        return True
    else:
        return False

s=input().split(',')
list=[]
print(s)
for i in s:
    if a_z(i) and A_Z(i) and number(i) and length(i) and character(i):
        list.append(i)

print(','.join(list))
