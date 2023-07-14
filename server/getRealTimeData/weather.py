import requests
from bs4 import BeautifulSoup

url = 'http://www.weather.com.cn'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

city = soup.find(id='cityName')  # 获取城市名称
print(city)