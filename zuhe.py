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
    huihang = stock("03698", "徽商银行", "hk", 300)
    zuhe.append(huihang)

    maotai = stock("600519", "贵州茅台", "sh", 310)
    zuhe.append(maotai)

    minshenga = stock("600016", "民生银行A", "sh", 80)

    zhaohang = stock("600036", "招商银行", "sh", 3000)
    zuhe.append(zhaohang)

    fuyao = stock("600660", "福耀玻璃", "sh", 700)
    zuhe.append(fuyao)

    pingan = stock("601318", "中国平安", "sh", 300)
    zuhe.append(pingan)

    donge = stock("000423", "东阿阿胶", "sz", 300)
    zuhe.append(donge)

    wuliang = stock("000858", "五粮液", "sz", 400)
    zuhe.append(wuliang)

    sanjin = stock("002275", "桂林三金", "sz", 200)
    zuhe.append(sanjin)

    yanghe = stock("002304", "洋河股份", "sz", 200)
    zuhe.append(yanghe)

    zhonghang = stock("03988", "中国银行", "hk", 7000)
    zuhe.append(zhonghang)

    nonghang = stock("01288", "农业银行", "hk", 6000)
    zuhe.append(nonghang)

    xinda = stock("01359", "中国信达", "hk", 15000)
    zuhe.append(xinda)

    fengxiang = stock("900905", "老凤祥", "sh", 1200, "usd")
    zuhe.append(fengxiang)

    tanmu = stock("00837", "谭木匠", "hk", 7500)
    zuhe.append(tanmu)

    baiyun = stock("00874", "白云山", "hk", 2000)
    zuhe.append(baiyun)

    kangchen = stock("01681", "康臣药业", "hk", 5000)
    zuhe.append(kangchen)

    bishou = stock("01830", "必瘦站", "hk", 28000)
    zuhe.append(bishou)

    haohai = stock("06826", "昊海生科", "hk", 600)
    zuhe.append(haohai)

    jinjie = stock("03918", "金界控股", "hk", 14000)
    zuhe.append(jinjie)

    minshengh = stock("01988", "民生银行H", "hk", 100)
    zuhe.append(ajiah("民生银行H+A",minshengh,minshenga))

    huanqiu = stock("02666", "环球医疗", "hk", 15000)
    zuhe.append(huanqiu)

    jianhang = stock("00939", "建设银行", "hk", 2000)
    zuhe.append(jianhang)

    tianli = stock("01773", "天立教育", "hk", 30000)
    zuhe.append(tianli)

    return zuhe