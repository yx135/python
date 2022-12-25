import re
a = input('Enter passwords: ').split(',')
pass_pattern = re.compile(r"^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[$#@]).{6,12}$")
for i in a:
    if pass_pattern.fullmatch(i):
        print(i)