import pandas as pd

URL = 'https://static.runoob.com/download/sites.json'
df = pd.read_json(URL)
print(df.to_string)