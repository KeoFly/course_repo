import requests
from bs4 import BeautifulSoup

header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:94.0) Gecko/20100101 Firefox/94.0', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9, image/avif,image/webp,/;q=0.8'}
page = requests.get('https://www.afi.com/afis-100-years-100-movies/', headers=header)

soup = BeautifulSoup(page.text, 'html.parser')

films = soup.find_all('h6', {'class': 'q_title'})

film_list = [film.text for film in films]

for film in film_list:
    print(film)