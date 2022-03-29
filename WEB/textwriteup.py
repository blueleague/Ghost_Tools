# 调用依赖库
import os
import requests
from PIL import Image

# 会话保持
session = requests.session()
# 导入 Cookie
cookie = {"PHPSESSID": "av3fe459fu80v1h4b8432a50g0"}

# 设置IP和端口
ipport = '39.104.76.137:18068'
url0 = 'http://'+str(ipport)+'/ilegaltext500.php'
html = requests.get(url=url0, cookies=cookie)
# print(html.content.decode().split('文本编号：')[1])

# 分段检查合规
i = 1
sum = 0
while i < 501:
    # print(html1.content.decode())
    if '违规蚊苯' not in html.content.decode().split('文本编号：')[i] and '不良鑫玺' not in html.content.decode().split('文本编号：')[i]:
        pass
    else:
        sum = sum + i
    i = i + 1

print(sum)

# 获取图片验证码
url2 = 'http://'+str(ipport)+'/image.php'
html = requests.get(url=url2, cookies=cookie)
with open('image.php', 'wb') as file:
    file.write(html.content)
os.rename('image.php', 'image.png')

# 输入验证码
code = input('请输入图片验证码：')
print(code)

# 提交结果
os.remove('image.png')
os.remove('image.png')
data = {'sum': sum, 'code': code}
url3 = 'http://'+str(ipport)+'/result500.php'
html = requests.post(url=url3, data=data, cookies=cookie)
print(html.content.decode())
