def check(x):                   # check function returns true if divisible by 5
    return int(x,2)%5 == 0      # int(x,b) takes x as string and b as base from which
                                # it will be converted to decimal
data = input().split(',')

data = list(filter(check,data)) # in filter(func,object) function, elements are picked from 'data' if found True by 'check' function
print(",".join(data))