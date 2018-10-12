# -*- coding:utf-8 -*-
import requests
from lxml import etree
import pandas as pd
import os


"""
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
url_xp = '//*[@id="td_uid_9_5bbc55cc72b41"]/div//h3/a/@href'
title_xp = '//*[@id="td_uid_9_5bbc55cc72b41"]/div//h3/a/@title'
channel_xp = '//*[@id="td_uid_9_5bbc55cc72b41"]/div/div[1]/div[2]/div/div[1]/a/text()'
datetime_xp = '//*[@id="td_uid_9_5bbc55cc72b41"]/div/div[1]/div[2]/div/div[2]/span[2]/time/@datetime'
# print(html_data.content)
data = etree.HTML(html_data.content)
url_data = data.xpath(url_xp)
title_data = data.xpath(title_xp)
channel_data = data.xpath(channel_xp)
datetime_data = data.xpath(datetime_xp)

########################  详情页  ##########################
text_data = []
content_url = 'https://smartereum.com/37171/bitcoin-btc-latest-update-cryptos-trade-sideways-as-bitcoin-btc-declines-by-more-than-4-xrp-and-ethereum-drops-9-percent-bitcoin-btc-news-today-btc-usd-price-today/'
content_html_data = requests.get(content_url, headers=headers)
content_xp = '//*[@class="td-post-content"]/*'
data = etree.HTML(content_html_data.content)
info_data = data.xpath(content_xp)
print(info_data)
info = ''
pic_num = 0
url_num = 0
for i in info_data:
    if i.tag == 'p' and i.text:
        info += i.text.encode('ascii', 'ignore').decode('ascii') + ' '
    elif i.tag == 'h2':
        ll = i.xpath('//strong/text()')[0] + ' ???bold??? '
        info += ll.encode('ascii', 'ignore').decode('ascii') + ' '
    else:
        url = i.xpath('/*[position()<24]//a')
        print(len(url))
        pic = i.xpath('/*[position()<24]//img ')
        print(len(pic))



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
df['Source'] = ['source' for _j in range(len(url_data)) ]
# HasVideo (boolean): 0 or 1
df['HasVideo'] = [1 for k in range(len(url_data))]
df['Datetime'] = [datetime_data[0] for j in range(len(url_data))]
# PicNum (int)
df['PicNum'] = [100 for _k in range(len(url_data))]
df['URLNum'] = [len(url_data) for i in range(len(url_data))]

df['Summary'] = ['summary' for z in range(len(url_data))]


df['Content'] = text_data
# df.to_csv('Demo1.csv', index=0, encoding='gb2312')
"""
class SmartereumSpider(object):
    def __init__(self):
        self.url = 'https://smartereum.com/cryptocurrency/bitcoin/'
        self.base_path = os.path.abspath(os.curdir)
        self.headers = {'Accept': '*/*',
               'Accept-Language': 'en-US,en;q=0.8',
               'Cache-Control': 'max-age=0',
               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
               'Connection': 'keep-alive',
               'Referer': 'http://www.baidu.com/'
               }

        self.titleList = []

        self.summaryList = []

        self.contentList = []

        self.channelList = []
        self.sourceList = []
        self.datetimeList = []
        self.picNumList = []
        self.hasVideoList = []
        self.urlNumList = []


    def dfContent(self, dataList):
        path = self.base_path + '/smartereum_2018-01-01_2018-12-31_content.csv'
        isExists = os.path.exists(path)
        if not isExists:
            df = pd.DataFrame(columns=['Content'])
            df['Content'] = dataList
            df.to_csv(path, index=0, encoding='gb2312')
        else:
            oldData = pd.read_csv(path)
            df = pd.DataFrame(columns=['Content'])
            df['Content'] = dataList
            result = oldData.append(df)
            result.to_csv(path, index=0, encoding='gb2312')

    def dfSummary(self, dataList):
        path = self.base_path + '/smartereum_2018-01-01_2018-12-31_summary.csv'
        isExists = os.path.exists(path)
        if not isExists:
            df = pd.DataFrame(columns=['Summary'])
            df['Summary'] = dataList
            df.to_csv(path, index=0, encoding='gb2312')
        else:
            oldData = pd.read_csv(path)
            df = pd.DataFrame(columns=['Summary'])
            df['Summary'] = dataList
            result = oldData.append(df)
            result.to_csv(path, index=0, encoding='gb2312')

    def dfTitle(self, dataList):
        path = self.base_path + '/smartereum_2018-01-01_2018-12-31_title.csv'
        isExists = os.path.exists(path)
        if not isExists:
            df = pd.DataFrame(columns=['Title'])
            df['Title'] = dataList
            df.to_csv(path, index=0, encoding='gb2312')
        else:
            oldData = pd.read_csv(path)
            df = pd.DataFrame(columns=['Title'])
            df['Title'] = dataList
            result = oldData.append(df)
            result.to_csv(path, index=0, encoding='gb2312')

    def dfOther(self, dataDict):
        #  dataDict 是 key :A1 A2 A3 A4 A5 A6

        path = self.base_path + '/smartereum_2018-01-01_2018-12-31_other.csv'
        isExists = os.path.exists(path)
        if not isExists:
            df = pd.DataFrame(columns=['Channel', 'Source', 'DateTime', 'PicNum', 'HasVideo', 'URLNum'])
            df['Channel'] = dataDict['Channel']
            df['Source'] = dataDict['Source']
            df['DateTime'] = dataDict['DateTime']
            df['PicNum'] = dataDict['PicNum']
            df['HasVideo'] = dataDict['HasVideo']
            df['URLNum'] = dataDict['URLNum']
            df.to_csv(path, index=0, encoding='gb2312')
        else:
            oldData = pd.read_csv(path)
            df = pd.DataFrame(columns=['Channel', 'Source', 'DateTime', 'PicNum', 'HasVideo', 'URLNum'])
            df['Channel'] = dataDict['Channel']
            df['Source'] = dataDict['Source']
            df['DateTime'] = dataDict['DateTime']
            df['PicNum'] = dataDict['PicNum']
            df['HasVideo'] = dataDict['HasVideo']
            df['URLNum'] = dataDict['URLNum']
            result = oldData.append(df)
            result.to_csv(path, index=0, encoding='gb2312')

    # 获取前5块位置的url列表
    def getUrlList_first5(self, xpathData):
        urlList_xp = "//*[@class='td-meta-align']//h3/a/@href"
        urlList = xpathData.xpath(urlList_xp)
        return urlList

    def getTitle(self, xpathData):
        title_xp = "//*[@class='td-meta-align']//h3/a/@title"
        titleList = xpathData.xpath(title_xp)
        # print(titleList)
        self.titleList = titleList

    def getChannel(self, xpathData):
        channel_xp = '//*[@class="td-pb-span12"]//div/a/text()'
        channelList = xpathData.xpath(channel_xp)
        self.channelList = channelList

    def getDatetime(self, xpathData):
        datetime_xp = '//span[@class="td-post-date td-post-date-no-dot"]/time/@datetime'
        datetime_l = xpathData.xpath(datetime_xp)[0]
        self.datetimeList.append(datetime_l)
        # print(self.datetimeList)

    def getSummary(self, xpathData):
        self.summaryList = ['' for i in range(len(self.titleList))]

    def getSource(self):
        self.sourceList.append('smartereum')

    def getContent(self, xpathData):
        content_xp = '//*[@class="td-post-content"]/*'
        info_data = xpathData.xpath(content_xp)
        info = ''
        pic_num = 0
        url_num = 0
        for i in info_data:
            if i.tag == 'p' and i.text:
                info += i.text.encode('ascii', 'ignore').decode('ascii') + ' '
            elif i.tag == 'h2':
                ll = i.xpath('//strong/text()')[0] + ' ???bold??? '
                info += ll.encode('ascii', 'ignore').decode('ascii') + ' '
            else:
                url = i.xpath('/*[position()<24]//a')
                print(len(url))
                pic = i.xpath('/*[position()<24]//img ')
                print(len(pic))

    def run(self):
        html_data = requests.get(self.url, headers=self.headers)
        data = etree.HTML(html_data.content)
        # 一、smartereum.com 前面5块位置的信息
        # 1.获取列表页信息
        # 1.1 获取列表页地址
        urlList = self.getUrlList_first5(data)
        # print(urlList)
        # 1.2 获取标题
        self.getTitle(data)
        # 1.3 获取新闻概要 如果没有 用空
        self.getSummary(data)
        # 1.4 获取新闻索引 小标记 channel
        self.getChannel(data)
        # 2.获取详情页信息
        for url in urlList:
            infoHtml_data = requests.get(url, headers=self.headers)
            info_data = etree.HTML(infoHtml_data.content)
            # 2.1 获取详情页的时间
            self.getDatetime(info_data)
            # 2.2 获取新闻来源
            self.getSource()
            # 2.3 获取新闻 详情
            self.getContent(info_data)


        print('datetime:',self.datetimeList)
        print('titleList:', self.titleList)
        print('channelList:', self.channelList)
        print('summaryList:', self.summaryList)
        print('sourceList:', self.sourceList)
        # 二、获取后边 俩列的信息

        pass


if __name__ == '__main__':
    SmartereumSpider().run()


