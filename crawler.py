import requests
from bs4 import BeautifulSoup
import random
random.random()
from time import sleep
import random


path = 'https://vp.fact.qq.com/loadmore?artnum=0&page='
url = path + '0'
content = requests.get(url)
d = content.json()
d['content'][0]

print(*range(61))

jsons = []
for i in range(61):
    print(i)
    sleep(random.random())
    path = 'https://vp.fact.qq.com/loadmore?artnum=0&page='
    url = path + str(i)
    content = requests.get(url)
    d = content.json()
    for j in d['content']:
        jsons.append(j)

len(jsons)
import pandas as pd
df = pd.DataFrame(jsons)
df.head()

df.to_excel('../data/vpqq2020-06-06.xlsx')
