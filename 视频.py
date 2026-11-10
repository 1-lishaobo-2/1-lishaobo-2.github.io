import requests

url = "http://video.com/movie.mp4"

resp = requests.get(url)
with open("movie.mp4", "wb") as f:
        f.write(resp.content)
print('保存成功')


import os

names = ["流行音乐", "古典音乐", "摇滚音乐"]

base_dir = "music"

for name in names:
        folder_path = os.path.join(base_dir, name)

        if not os.path.exists(folder_path):
                os.makedirs(folder_path)
                print(f"已创建文件夹：{folder_path}")

print("\n音乐分类文件夹创建完成！")


import os
import requests

videos = [
        {
                "name": "video1",
                "url": "https://www.w3school.com.cn/example/html/mov_bbb.mp4"
        },
        {
                "name": "video2",
                "url": "https://www.w3school.com.cn/example/html/mov_bbb.mp4"
        },
        {
                "name": "video3",
                "url": "https://www.w3school.com.cn/example/html/mov_bbb.mp4"
        }
]

folder_name = "videos"
if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"文件夹 '{folder_name}' 已创建。")

for video in videos:
        name = video["name"]
        url = video["url"]

        file_path = os.path.join(folder_name, f"{name}.mp4")

with open(file_path, 'wb') as f:
        f.write(requests.get(url).content)
print(f"'{name}' 下载完成。")