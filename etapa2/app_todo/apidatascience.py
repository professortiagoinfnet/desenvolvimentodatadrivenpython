import httpx
import pandas as pd

url = "https://jsonplaceholder.typicode.com/users"
response = httpx.get(url)
data = response.json()

df = pd.DataFrame(data)
print(df)
print(df.columns)
print(df['name'])
