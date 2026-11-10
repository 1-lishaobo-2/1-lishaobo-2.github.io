import requests
from lxml import etree
import json
import time

# 搜索结果界面网址
sousuo_url = 'https://www.gequbao.com/s/周杰伦'
# 请求头(本节课所有请求都可用)
music_headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36'
}
# 发送请求, 得到搜索结果
sousuo_resp = requests.get(url=sousuo_url,headers=music_headers)
# 通过.text得到了一个带有html结构的字符串
# print(sousuo_resp.text)
# 将字符串变成html树
tree = etree.HTML(sousuo_resp.text)
# 定位所有歌曲的a标签, 得到一个列表
a_tags = tree.xpath('//a[@class="hover-zoom d-block text-decoration-none"]')
# print(a_tags)
# 循环a标签列表, 提取每个标签中的href【播放网址】和title【歌曲名称】的值
for a in a_tags:
    # 【较多同学对此处xpath的.有疑问】
    # .指的是当前a标签本身，找标签中href的值使用 /@href
    # xpath得到的是一个列表，所以要在后面加上[0]表示获取的是列表中的第一个元素
    detail_url = a.xpath('./@href')[0]
    # 完整的【播放网址】 前面需要拼接上https://www.gequbao.com
    detail_url = 'https://www.gequbao.com' + detail_url
    # 【歌曲名称】在a标签的title属性中
    music_name = a.xpath('./@title')[0]
    # print(f'【播放网址】: {detail_url}')
    # print(f'【歌曲名称】: {music_name}')
    print(f'开始下载{music_name}...')
    # 发送请求，获取【播放网址】的内容
    detail_resp = requests.get(url=detail_url, headers=music_headers)
    # print(detail_resp.text) # 得到的是一个html网页的数据

    # 得到响应的html字符串数据
    detail_result = detail_resp.text
    # 通过字符串的方法，提取play_id的值
    """
    【注意事项】：在浏览器的响应中显示的是 \u0022, 但在pycharm中得到的数据是 \\u0022
    """
    # 通过\\u0022play_id\\u0022:\\u0022唯一性将全篇源码分割两份
    str1 = detail_result.split('\\u0022play_id\\u0022:\\u0022')[1]
    # print(str1)
    # 继续用\\u0022来分割，第一个内容索引为0就是最干净的id
    play_id = str1.split('\\u0022')[0]
    # print(play_id)

    # 2. 第二次请求, 携带这个唯一id去发post请求, 从响应的数据中提取这首歌的下载地址
    # 【参数是字典格式】
    play_data = {
        "id": play_id
    }
    # 请求网址
    play_url = 'https://www.gequbao.com/member/common-play-url'
    # 携带参数发送post请求
    play_resp = requests.post(url=play_url, data=play_data, headers=music_headers)
    # print(play_resp.text) # 得到的是json字符串
    # 将json字符串转为字典
    result = json.loads(play_resp.text)
    # 音乐下载链接
    music_url = result['data']['url']

    # 3. 第3次请求，下载音乐
    music_resp = requests.get(url=music_url, headers=music_headers)
    # 保存音乐
    """
    代码合并后,保存的音乐名要改成之前提取到的music_name
    """
    with open(f'{music_name}.mp3', 'wb') as f:
        f.write(music_resp.content)

    print(f'{music_name}下载完成')
    time.sleep(10)







































