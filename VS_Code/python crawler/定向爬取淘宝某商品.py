from bs4 import BeautifulSoup
import requests
import re
import xlwt
import time


def getHTML(url,head):
    try:
        r = requests.get(url, headers = head)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return ''


def getInfo(html, lt):
    try:
        # 通过正则表达式来直接从html文件中搜索想要爬取的信息，此处商品名称以及商品价格与raw_title和view_price呈现键值关系
        price_list = re.findall(r'\"view_price\":\"[\d\.]*\"', html)
        name_list = re.findall(r'\"raw_title\":\".*?\"', html)
        for i in range(0, len(price_list)):
            price = eval(price_list[i].split(':')[1])
            name = eval(name_list[i].split(':')[1])
            # 将名称与价格形成一个列表存进我们自己创建的清单中
            lt.append([name, price])
    except:
        print('')


def creatExcel(lt):
    f = xlwt.Workbook(encoding = 'utf-8')
    sheet1 = f.add_sheet('商品', cell_overwrite_ok = False)
    # 设置格式
    sheet1.col(0).width = 256 * 75
    sheet1.col(1).width = 256 * 25
    sheet1.write(0, 0, '商品名称')
    sheet1.write(0, 1, '商品价格')
    for i in range(0, len(lt)):
        for num in range(0,2):
            sheet1.write(i+1, num, lt[i][num])

    f.save("C://Users//Lenovo//Desktop//滚去学习！//大三//商品清单.xls")


def main(num, goods):
    root_url = 'https://s.taobao.com/search?q=' + goods
    goodsList = []
    # 替换掉request的headers，已达到欺骗淘宝服务器我已经登录的目的
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/80.0.3987.132 Safari/537.36 Edg/80.0.361.66",
        "Cookie": "cna=q9jgFnQ+3hsCAd7RR90eajOX; thw=cn; uc3=vt3=F8dBxd30snQMq4%2BOaPY%3D&nk2=1HMExSKp&id2=UNN66cUmrns7"
                  "%2Bg%3D%3D&lg2=UtASsssmOIJ0bQ%3D%3D; lgc=%5Cu53CD%5Cu9633%5Cu6811; "
                  "uc4=id4=0%40UgQyfnBlcKyMG2Qe2mXfJHi7xAb9&nk4=0%401qLISaynZ0fwOz7T%2BlazC6w%3D; "
                  "tracknick=%5Cu53CD%5Cu9633%5Cu6811; _cc_=UIHiLt3xSw%3D%3D; tg=0; "
                  "enc=zJ8zFC1CxU%2FFId9WOO7yvJ6fZIpmvom2N4z4MS2rJ7lglloAXTV5buAYRfABV6vJ6YyoNMtw%2FATYqfpflXDlxQ%3D%3D; "
                  "tfstk=cDxFBP65TDnEcmgwoisPNsJmHSuCaUpHElWf-EVn2sirbc_hgsmawOD_wOW76CQh.; hng=CN%7Czh-CN%7CCNY%7C156; "
                  "mt=ci=-1_0; miid=1721623009917751890; _m_h5_tk=6f3942fcedb7d7d610a525f6f7582b13_1584025959856; "
                  "_m_h5_tk_enc=f27062ae8580a846729e1ea4ceb8e66d; v=0; t=c2caca4c21ee631b6641f99d870dc5cc; "
                  "cookie2=159a31c49b28cf4cb77cffb2f9082bfc; _tb_token_=4038383f38b7; alitrackid=www.taobao.com; "
                  "lastalitrackid=www.taobao.com; _samesite_flag_=true; JSESSIONID=A4CF57BAED381665D0E1FB3C1C3926FB; "
                  "uc1=cookie14=UoTUPvXe7zwP8g%3D%3D; "
                  "l=dBSaC_YnQukIriGBBOfZIKoJaLbTaIRb8kPPu4dthICPOQCH5J_NWZ4fb0LMCn1V3sOwJ37doObTBzTaxyUB5jMUaaYCgsDpDdTeR"
                  "; isg=BH9_AL51HccGQRnwMJL3RAjADlMJZNMGLLevbRFMwS51IJ6iGDfpVnR6YnDeY6t- "
    }
    for i in range(num):
        try:
            url = root_url + '&s=' + str(44*i)
            html = getHTML(url, headers)
            getInfo(html, goodsList)
        except:
            continue
    creatExcel(goodsList)


temp = str(input("想要搜索什么商品："))
num = int(input("请输入想要多少页商品的数据："))
start = time.time()
main(num, temp)
end = time.time()
print("总计时间：", end - start)