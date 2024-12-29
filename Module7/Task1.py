import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

url = 'https://mfd.ru/currency/?currency=USD'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/98.0.4758.102 Safari/537.36'}

resp = requests.get(url, headers=headers)

soup = BeautifulSoup(resp.text, 'html.parser')

tmp_data = soup.find('table', {'class': 'mfd-currency-table'})
data = tmp_data.find_all('td')

rate = [rt.text for rt in data]
rates = []
dates = []

for i in range(1, len(rate), 3):
    rates.append(float(rate[i]))
for i in range(0, len(rate), 3):
    dates.append(rate[i][2:])
dates = dates[::-1]
rates = rates[::-1]

plt.plot(dates, rates)
plt.show()
