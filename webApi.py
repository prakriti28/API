import requests
base_url="https://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=439d4b804bc8187953eb36d2a8c26a02"
api_key="439d4b804bc8187953eb36d2a8c26a02"
city =input()
url=f"{base_url}?q={city }&appid={api_key}"
# print(url)
res=requests.get(url)
res.headers
res.content
result=res.json()
print("Temperature: "+str(result['main']['temp']))
print("Minimum temperature: "+str(result['main']['temp_min']))
print("Maximum temperature: "+str(result['main']['temp_max']))
print("Humidity: "+str(result['main']['humidity']))
print("Pressure: "+str(result['main']['pressure']))

