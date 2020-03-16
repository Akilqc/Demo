import requests
import os
url = "https://i-f.pximg.net/img-master/img/2020/03/11/00/42/15/80036479_p0_master1200.jpg"
root = "C://Users//Lenovo//Desktop//Pixiv//"
# 以'/'为标准进行分割 取最后一个
path = root + url.split('/')[-1]
try:
    # 判断根目录文件夹是否存在，如果不存在就进行新建文件夹操作
    if not os.path.exists(root):
        os.mkdir(root)
    # 判断根目录文件夹里是否存在目标文件
    if not os.path.exists(path):
        r = requests.get(url)
        with open (path, 'wb') as f:
            f.write(r.content)
            f.close()
            print('文件保存成功')
    else:
        print("文件已被保存")
except:
    print("爬取失败")