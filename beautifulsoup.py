import requests
from bs4 import BeautifulSoup 
import requests
from bs4 import BeautifulSoup 

url = 'https://vp.fact.qq.com/home'
content = requests.get(url)
soup = BeautifulSoup(content.text, 'html.parser') 
help(requests.get)

print(soup.prettify())

soup.select('body > p.title > b')[0].text

soup.select('title')[0].text
soup.select('b')
soup.select('a')
soup.select('.title')
soup.select('.sister')
soup.select('.story')
soup.select('#link1')
soup.select('#link1')[0]['href']
soup.select('p #link1')
soup.select("head > title")
soup.select("body > p")
#soup('p')
soup.find_all('p')
soup.find_all('p') 
[i.text for i in soup('p')]
for i in soup('p'):
    print(i.text)
    
for tag in soup.find_all(True):
    print(tag.name)

soup('body') # or soup.body
soup('head') # or soup.head
soup('title') 
soup('p')
soup.p

path = 'https://vp.fact.qq.com/loadmore?artnum=0&page='
url = path + '0'
content = requests.get(url)
d = content.json()
