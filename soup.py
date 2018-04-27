from bs4 import BeautifulSoup
import urllib.request

html = urllib.request.urlopen('https://en.wikipedia.org/wiki/List_of_programming_languages').read()

# soup = BeautifulSoup(html, 'html.parser')
soup = BeautifulSoup(html, 'lxml')
divs = soup.findAll('div', class_='columns') 

for ul in divs:
    for li in ul.findAll('li'):
        a = li.find('a')
        if a is None:
            print('nope')
        else:
            print("%s's url is %s" % (a.text, a.attrs['href']))
