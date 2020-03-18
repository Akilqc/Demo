import requests
import bs4
from bs4 import BeautifulSoup
import xlwt
import time


# 获取html
def getHTML(url):
    # noinspection PyBroadException
    try:
        r = requests.get(url, timeout = 20)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return ""


# 获取排名的表头
def getTitle(html, list):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('thead').children:
        if isinstance(tr, bs4.element.Tag):
            temp = tr.find_all('th')
    child = temp[4].children

    # 获取表头中不包含折叠部分的字符串
    for i in range(0, (len(temp) - 1)):
        list.append(temp[i].string)

    # 获取第五个折叠的字符串
    for i in child:
        if isinstance(i, bs4.element.Tag):
            temp_list = i.find_all('option')
    for i in range(0, len(temp_list)):
        list.append(temp_list[i].string)


#  获取排名的数据
def fillList(html, list):
    soup = BeautifulSoup(html, "html.parser")
    a = 0
    td_list = []
    temp_list = []
    for item in soup.find('tbody').children:
        # 除掉第一个的空子辈
        if a == 0:
            a += 1
            continue
        else:
            if isinstance(item, bs4.element.Tag):  # 判断是否为Tag属性，避免将部分转义符写入
                td_list = item.find_all('td')
            for i in range(0, len(td_list)):
                temp_list.append(td_list[i].string)
            list.append(temp_list)
            temp_list = []  # 每获取一个大学的信息后都需要清空列表，使得list列表中的元素为列表类型
            a += 1


def printList(list, num):
    title = "{0:^25}\t{1:{4}^25}\t{2:^25}\t{3:^25}"
    # chr(12288)表示的是中文空格，当中英文混合输出时，会出现无法对齐的现象，这时使用chr(12288)来填充就可以很好地解决问题
    print(title.format("排名", "学校名称", "总分", "毕业生就业率", chr(12288)))
    for i in range(num):
        print(title.format(list[i][0], list[i][1], list[i][2], list[i][3], chr(12288)))


# 输出到Excel文件中
def creatExcel(datalist, titlelist):
    # 新建excel文件，注意改变encoding
    f = xlwt.Workbook(encoding = 'utf-8')
    sheet1 = f.add_sheet('2019大学排名以及就业率', cell_overwrite_ok = False)
    # 设置格式
    for i in range(0, len(titlelist)):
        sheet1.col(i).width = 256 * 25
    # 写第一行
    for i in range(0, len(titlelist)):
        sheet1.write(0, i, titlelist[i])
    # 写后面的数据行
    for num in range(0, len(data_list)):
        for i in range(0, len(datalist[num])):
            sheet1.write(num + 1, i, datalist[num][i])

    f.save("C://Users//Lenovo//Desktop//滚去学习！//大三//中国大学2019综合排名及指标得分.xls")



start = time.time()
data_list = []
title_list = []
url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2019.html"
text = getHTML(url)
getTitle(text, title_list)
fillList(text, data_list)
creatExcel(data_list, title_list)
end = time.time()
print("用时：", end - start)


