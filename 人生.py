import random

events = ['打游戏','努力工作','体力耗尽']
for i in range(1,4):
    NBA = random.choice(events)
    if NBA == '体力耗尽':
        print(f'第{i}天：体力耗尽，结束生活')
        break
    else:
        print(f'第{i}天：发生了{NBA}事件')

