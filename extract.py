import padans as pd
import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")
data = response.json()

df= pd.DataFrame(data)
df=df[['id','name','username','email','address']]

print("The data is extracted successfully")
print(df)