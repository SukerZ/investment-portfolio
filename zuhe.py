from hanshu import *

class stock(object):
    def __init__(self, code, name, mtk, num, coin = "rmb"):
        self.code = code; self.name = name
        self.mtk = mtk; self.num = num
        self.coin = coin
        self.price = get(self.code, self.mtk, self.coin)
        self.value = self.price * self.num

class ajiah(stock):
    def __init__(self, name, agu, hgu):
        self.name = name
        self.value = agu.value + hgu.value

def zuhe():
    zuhe = []

    maotai = stock("600519", "贵州茅台", "sh", 310)
    zuhe.append(maotai)

    zhaohang = stock("600036", "招商银行A", "sh", 3700)
    zuhe.append(zhaohang)

    pingan = stock("601318", "中国平安A", "sh", 300)
    zuhe.append(pingan)

    wuliang = stock("000858", "五粮液", "sz", 400)
    zuhe.append(wuliang)

    yanghe = stock("002304", "洋河股份", "sz", 200)
    zuhe.append(yanghe)

    zhonghang = stock("03988", "中国银行H", "hk", 7000)
    zuhe.append(zhonghang)

    nonghang = stock("01288", "农业银行H", "hk", 6000)
    zuhe.append(nonghang)

    xinda = stock("01359", "中国信达H", "hk", 15000)
    zuhe.append(xinda)

    fengxiang = stock("900905", "老凤祥B", "sh", 1200, "usd")
    zuhe.append(fengxiang)

    tanmu = stock("00837", "谭木匠", "hk", 7500)
    zuhe.append(tanmu)

    baiyun = stock("00874", "白云山H", "hk", 2000)
    zuhe.append(baiyun)

    kangchen = stock("01681", "康臣药业", "hk", 5000)
    zuhe.append(kangchen)

    bishou = stock("01830", "必瘦站", "hk", 24000)
    zuhe.append(bishou)

    jinjie = stock("03918", "金界控股", "hk", 16000)
    zuhe.append(jinjie)

    minshengh = stock("01988", "民生银行H", "hk", 100)
    zuhe.append(minshengh)

    huanqiu = stock("02666", "环球医疗", "hk", 15000+1000)
    zuhe.append(huanqiu)

    jianhang = stock("00939", "建设银行H", "hk", 2000)
    zuhe.append(jianhang)

    tianli = stock("01773", "天立教育", "hk", 47000)
    zuhe.append(tianli)

    return zuhe