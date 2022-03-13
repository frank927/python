import requests
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
};
page = requests.get('http://www.cubadebate.cu/categoria/noticias/', headers=headers)
page
page.content
soup = BeautifulSoup(page.content, 'html.parser')
t=soup.title.string
div_t = soup.find_all('div', class_=('title'))
div_c = soup.find_all('div', class_=('excerpt'))

cant=((len(div_t+div_c))/2)
print()
print(t)
print()
print('Hay '+str(cant)+' noticias publicadas.')
print()
for i in soup.find_all('div', class_=('title','excerpt')):
        print(i.get_text())
        print()
