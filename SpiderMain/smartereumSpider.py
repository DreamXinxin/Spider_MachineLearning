# -*- coding:utf-8 -*-
import requests
from lxml import etree

headers = {'Accept': '*/*',
               'Accept-Language': 'en-US,en;q=0.8',
               'Cache-Control': 'max-age=0',
               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
               'Connection': 'keep-alive',
               'Referer': 'http://www.baidu.com/'
               }


url = 'https://smartereum.com/cryptocurrency/bitcoin/'

html_data = requests.get(url, headers=headers)


xp = '//*[@id="td_uid_9_5badf47708b49"]/div/div[1]/div[1]/div/a/@title'
info_xp = ''
data = etree.HTML(html_data.content)
print(data)
h_data = data.xpath(xp)
for i in h_data:
    print(i)


