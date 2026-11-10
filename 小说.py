import requests
from lxml import etree
import time

#首先先获取url
kaiyangurl = 'https://www.diandingnnn.cc/ddk92482/'

kaiyangheaders = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36'
}

#发送请求
response = requests.get(url=kaiyangurl,headers=kaiyangheaders)
#把这个网站的内容，转为一棵可以爬下来的树
data = etree.HTML(response.text)


#用xpah解析内容 <a href="/ddk92482/72241986.html">第二十四章 相赠</a>
# 第二十四章 相赠 需要用a.text()
#href="/ddk92482/72241986.html" 需要 @href来找
urls = data.xpath('//div[@class="listmain"]//dd/a/@href')
# print(urls)

#正常网址 https://www.diandingnnn.cc/ddk92482/ + /ddk92482/88950294.html
# https://www.diandingnnn.cc/ddk92482/88950294.html
# 每次循环就能下一章
count = 0
for url in urls[12:22]:
    #这就是拼好以后的网址了
    new_url = 'https://www.diandingnnn.cc'+ url
    # print(new_url)
    # 请求网络--获得response--解析response--保存本地
    #这是访问每一章的内容
    new_response = requests.get(url=new_url,headers=kaiyangheaders)
    #每一章的提取标题，提取文本
    new_data = etree.HTML(new_response.text)
    #从里面去找内容
    new_biaoti = new_data.xpath('//h1/text()')[0]

    #找内容
    new_zhengwen = new_data.xpath('//div[@id="content"]/text()')
    # print(new_zhengwen)
    #保存每一行的内容
    for hang in new_zhengwen:
        with open(f'剑来/{new_biaoti}.txt','a',encoding='utf-8') as f:
            f.write(hang+'\n')
    count = count+1
    print(f'第{count}章已经下载完成')
    time.sleep(2)








