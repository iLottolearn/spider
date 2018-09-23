import json
from urllib import parse, request

keyword = input("请输入你要查询的单词（英文或中文）：")
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
Form_Data = {
"i": keyword,
"from":"AUTO",
"to":"AUTO",
"smartresult":"dict",
"client":"fanyideskweb",
"salt":"1537702371370",
"sign":"15e8af80518f09b6d5a1593d483c4137",
"doctype":"json",
"version":"2.1",
"keyfrom":"fanyi.web",
"action":"FY_BY_REALTIME",
"typoResult":"false",
}

data = parse.urlencode(Form_Data).encode("utf-8")
response = request.urlopen(url,data)
html = response.read()
results = json.loads(html)
result = results['translateResult'][0][0]['tgt']
print("翻译的结果为：%s"%result)