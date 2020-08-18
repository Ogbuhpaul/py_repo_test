import requests

x = requests.get('https://openweathermap.org/api')

print(x.text)
