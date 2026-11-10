import requests
import time


def fetch_data(url, max_retries=3):


    for i in range(max_retries):
        try:
            response = requests.get(url)

            if response.status_code == 200:
                return True
            else:
                raise Exception(f"非200状态码: {response.status_code}")

        except Exception as e:
            print(f"第 {i + 1} 次请求失败，错误信息：{e}")
            print("正在等待 2 秒后进行重试...")
            time.sleep(2)
            print('打印成功')