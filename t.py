import requests
from bs4 import BeautifulSoup


url = 'https://wallex.ir/calculator/btc-tmn'

response = requests.get(url)
response.raise_for_status()

html = response.text
soup = BeautifulSoup(html, 'html.parser')

elements = soup.find_all('p', class_='MuiTypography-root MuiTypography-body2 mui-mmyoxq')

value = elements[2].find('span').text

print(value)
