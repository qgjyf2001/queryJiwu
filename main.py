import requests
import os
from identifyNum import identify
import time
import datetime
session = requests.Session()
while (datetime.datetime.now().minute!=59):#文明抢课
    continue
headers = {'User-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
r1=session.get("http://115.25.136.17:9000/index.php",headers=headers).text
open('tmp.png','wb').write(session.get("http://115.25.136.17:9000/checkcode.php",headers=headers,stream=True).content)
auto=1#auto=0,手动;auto=1,自动
verifyCode=""
if (auto==0):
    os.system('tmp.png')
    verifyCode=input("请输入验证码")
else:
    verifyCode=identify()
    print(verifyCode)

#用户名和密码
data={'txtUid':'1937xxxx','txtPwd':'yourPassword','txtChk':verifyCode}

r2=session.post('http://115.25.136.17:9000/login.php',data,headers=headers).text
response=session.get('http://115.25.136.17:9000/elect.php',headers=headers)
r3=response.text.encode(response.encoding).decode(response.apparent_encoding)
print(r3)
url=[]
pos=r3.find('点击进入')
while (pos!=-1):
    pos=pos-50
    pos=r3.find('href',pos)
    rec=pos+5
    pos=r3.find('>',pos)
    url.append(r3[rec:pos])
    pos=pos+20
    pos=r3.find('点击进入',pos)
for urls in url:
    print('实验'+urls[len(urls)-2:])
    data={'iknow':'1'}
    response=session.post(('http://115.25.136.17:9000'+urls).replace('step=1','step=2'),data,headers=headers)
    r4=response.text.encode(response.encoding).decode(response.apparent_encoding)
    pos=r4.find('分组代号')
    while (pos!=-1):
        pos=r4.find('：',pos)
        rec=pos
        pos=r4.find('<',pos)
        print(r4[rec:pos]+':',end='')
        pos=r4.find('剩余空位',pos)
        rec=pos
        pos=r4.find('<',pos)
        print(r4[rec:pos])
        pos=r4.find('分组代号',pos)

mode=1#mode=0,抢课;mode>0,提前选课;others,不操作
if (mode>=0):
    while (True):
        data={'Result':'10221561'}
        response=session.post('http://115.25.136.17:9000/elect.php?type=0&step=3&eid=bas15',data=data,headers=headers)
        r5=response.text.encode(response.encoding).decode(response.apparent_encoding)
        print(r5)
        if (mode==1):
            break
        if (datetime.datetime.now().minute==2):#12点02分，抢课完成后关机
            os.system("shutdown -s")
        time.sleep(1)
