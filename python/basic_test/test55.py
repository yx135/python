import re

email = "2 cats and 3 dogs."
pattern = "(\d)"
ans = re.findall(pattern,email)
print(ans)