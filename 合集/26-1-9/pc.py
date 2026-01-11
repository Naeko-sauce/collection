import requests
import execjs

with open('a.js','r',encoding='utf-8') as f:
    js_code = f.read()

with open('aa.text','w',encoding='utf-8') as f:
    f.write(js_code)
ctx = execjs.compile(js_code)
r = ctx.call('window.indexcode.getResCode')
print(r)
cookies = {
    'MALLSSID': '6545535A6B375937734858375733307862486A594E4F514D7A303949392B57496877764E6A68494363414234444E50442B70797956513644356C657039664774',
}

headers = {
    'Accept': '*/*',
    'Accept-EncKey': r,
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://webapi.cninfo.com.cn',
    'Referer': 'https://webapi.cninfo.com.cn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36 Edg/143.0.0.0',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Microsoft Edge";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    # 'Cookie': 'MALLSSID=6545535A6B375937734858375733307862486A594E4F514D7A303949392B57496877764E6A68494363414234444E50442B70797956513644356C657039664774',
}

data = {
    'tdate': '2026-01-08',
    'market': 'SZE',
}

response = requests.post(
    'https://webapi.cninfo.com.cn/api/sysapi/p_sysapi1007',
      cookies=cookies, headers=headers, data=data,
       proxies={"http": None, "https": None}
      )
print("状态码:", response.status_code)
print("返回内容:")
print(response.text)
