from DrissionPage import ChromiumPage
from serverchan_sdk import sc_send
page = ChromiumOptions()

ghjhj = 4500

page.get('https://item.jd.com/100359969926.html')

title = page.ele('xpath://span[@class="sku-title-name"]').text
tpt = page.ele('xpath://span[@class="product-price--value"]').text
print(title)
if float(tpt) < ghjhj:
    print(f'当前价格是{float(tpt)}低于{ghjhj}')
sc_send(

            "SCT383773TtizsvkvyWGtUlDobeymihyMF",

            f"你关注的{title}已降价",

        )

page.wait(60)
page.quit()