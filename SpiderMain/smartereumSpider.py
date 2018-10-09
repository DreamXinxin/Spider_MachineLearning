# -*- coding:utf-8 -*-
import requests
from lxml import etree
import pandas as pd
import re


headers = {'Accept': '*/*',
               'Accept-Language': 'en-US,en;q=0.8',
               'Cache-Control': 'max-age=0',
               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
               'Connection': 'keep-alive',
               'Referer': 'http://www.baidu.com/'
               }


url = 'https://smartereum.com/cryptocurrency/bitcoin/'

html_data = requests.get(url, headers=headers)


# xp = '//*[@id="td_uid_9_5badf47708b49"]/div/div[1]/div[1]/div/a/text'
########################  列表页  #############################################
# TODO xpath中id值是定期发生变化的 如果数据为空 查看id值
url_xp = '//*[@id="td_uid_9_5bbc647b7aaeb"]/div//h3/a/@href'
title_xp = '//*[@id="td_uid_9_5bbc647b7aaeb"]/div//h3/a/@title'
channel_xp = '//*[@id="td_uid_9_5bbc647b7aaeb"]/div/div[1]/div[2]/div/div[1]/a/text()'
datetime_xp = '//*[@id="td_uid_9_5bbc647b7aaeb"]/div/div[1]/div[2]/div/div[2]/span[2]/time/@datetime'
# print(html_data.content)
data = etree.HTML(html_data.content)
url_data = data.xpath(url_xp)
title_data = data.xpath(title_xp)
channel_data = data.xpath(channel_xp)
datetime_data = data.xpath(datetime_xp)

########################  详情页  ##########################
text_data = []
content_url = 'https://smartereum.com/36835/bitcoin-btc-latest-update-new-ico-to-be-launched-on-the-blockchain-of-bitcoin-btc-later-this-year-bitcoin-btc-news-today-btc-usd-price-today/'
content_html_data = requests.get(content_url, headers=headers)
content_xp = '//*[@class="td-post-content"]/*'
data = etree.HTML(content_html_data.content)
info_data = data.xpath(content_xp)
# print(info_data)
info = ''
for i in info_data:
    if i.tag == 'p' and i.text:
        info += i.text.encode('utf-8').decode('utf-8') + '\n'
    elif i.tag == 'h2':
        ll = i.xpath('//strong/text()')[0] + '???bold???'
        info += ll.encode('utf-8').decode('utf-8') + '\n'



print(info)
text_data.append(info)
text_data.append('')
text_data.append('')
text_data.append('')
text_data.append('')

##################### 保存数据 #############################
df = pd.DataFrame()
df['Title'] = title_data
# TODO 应该是详情页的地址  目前是列表页中所有地址 需要更改
'Channel,Source,HasVideo,DateTime,PicNum,URLNum'
df['Channel'] = [channel_data[0] for _i in range(len(url_data))]
df['Summary'] = ['summary' for z in range(len(url_data))]
df['Source'] = ['source' for _j in range(len(url_data)) ]
# HasVideo (boolean): 0 or 1
df['HasVideo'] = [1 for k in range(len(url_data))]
df['Datetime'] = [datetime_data[0] for j in range(len(url_data))]
# PicNum (int)
df['PicNum'] = [100 for _k in range(len(url_data))]
df['URLNum'] = [len(url_data) for i in range(len(url_data))]
df['Content'] = text_data
df.to_csv('Demo.csv', index=0, encoding='utf-8')






