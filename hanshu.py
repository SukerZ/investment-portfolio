import pdb
import urllib.request
import re
import time
import json

def huilv():
    import http.client
    URL = "fx.cmbchina.com"
    try:
        httpClient = http.client.HTTPConnection(URL, 80, timeout=30); #pdb.set_trace()
        httpClient.request('GET', '/hq/')
        response = httpClient.getresponse()
        html = response.read().decode("utf-8")
        reg = re.compile(r"""
             <tr>\s*<td\s+class="fontbold">\s*(?P<name>\S+)\s*</td>\s*         #交易币
             <td\s+align="center">\s*(?P<unit>\d+)\s*</td>\s*                  #交易币单位
             <td\s+align="center"\s+class="fontbold">\s*(?P<base>\S+)\s*</td>\s*  #基本币
             <td\s*class="numberright">\s*(?P<midPrice>\d+\.\d+)\s*</td>\s*       #中间价
             <td\s*class="numberright">\s*(?P<sellPrice>\d+\.\d+)\s*</td>\s*                     #卖出价
             <td\s*class="numberright">\s*(?P<buyPrice1>\d+\.\d+)\s*</td>\s*                     #现汇买入价
             <td\s*class="numberright">\s*(?P<buyPrice2>\d+\.\d+)\s*</td>\s*                     #现钞买入价
             <td\s*align="center">\s*(?P<time>\d+:\d+:\d+)\s*</td>\s*                       #时间
             """, re.MULTILINE | re.X)
        rows = reg.findall(html); #pdb.set_trace()
        return float(rows[0][6])/100, float(rows[3][6])/100
    finally:
        if httpClient:
            httpClient.close()

hkd,usd = huilv()

def get(code, mkt, coin = "rmb"):
    code_par= mkt + code
    date = time.strftime('%Y-%m-%d', time.localtime(time.time()) )

    url = 'http://web.ifzq.gtimg.cn/appstock/app/kline/kline?_var=kline_day&param=%s,day,%s,%s,640,' % (code_par, date, date)

    cn = urllib.request.urlopen(url).readlines()[0].decode("utf-8"); #pdb.set_trace()
    js = re.search('(?<=kline_day=).*', cn).group(); #pdb.set_trace()
    jsparsed = json.loads(js); #pdb.set_trace()

    price = float(jsparsed["data"][code_par]["qt"][code_par][3])

    if mkt == "hk" or coin == "hkd":
        price *= hkd
    if coin == "usd":
        price *= usd

    return price

def qiuhe(zuhe):
    sum, X, labels=0, [], []
    for e in zuhe:
        sum += e.value
        X.append(e.value)
        labels.append(e.name)

    print("总市值： "+str(sum)+"元")
    return sum, X, labels

def biaoge(sum, X, labels):
    tmp = []
    for i in range(len(X)):
        tmp.append((X[i], labels[i]) )

    tmp.sort(key = lambda stock : stock[0], reverse = True)
    for i in range(len(tmp) ):
        print(i+1, tmp[i][1], "%.1f%%" % (tmp[i][0] / sum * 100) )

def bingtu(sun, X, labels):
    import matplotlib.pyplot as plt
    plt.rcParams['font.sans-serif'] = ["KaiTi"]  # 指定默认字体
    plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
    fig = plt.figure()
    plt.pie(X, labels=labels, autopct='%.1f%%')  # 画饼图（数据，数据对应的标签，百分数保留一位小数）
    date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    plt.title(date + "投资组合")
    plt.show()
    #fig.savefig("C:\\Users\\Administrator\\Desktop\\" + date + "投资组合.png")