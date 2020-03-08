from PIL import Image
import numpy as np
from matplotlib import pyplot
from pathlib import Path
import os


def picture_gray(filename, finalfilename):
    path_root_source = Path(r'C:\Users\Lenovo\Desktop\Pixiv')
    path_root_save = Path(r'C:\Users\Lenovo\Desktop\save')
    path_real = path_root_source / filename
    path_root_dir = path_root_save / filename
    os.makedirs(path_root_dir)
    path_gray1 = path_root_dir / filename
    path_gray2 = path_root_dir / finalfilename
    img = Image.open(path_real)

    # 转换为灰度图片
    img_convert = img.convert('L')
    a, b = img.size
    # img_convert = img_convert.resize((900,900))
    img_convert.save(path_gray1)

    # 得到灰度化后的像素矩阵
    img_martix = np.array(img_convert)
    # print(img_martix)
    m, n = np.shape(img_martix)

    # 计算每一个灰度级的出现次数
    img_gray_matrix = [0] * 256
    for row in img_martix:
        for pix in row:
            img_gray_matrix[pix] += 1
    # print(img_gray_matrix)

    # 求和，即计算每一灰度级的直方图
    img_gray_all = [0] * 256
    temp = 0
    for row in range(len(img_gray_matrix)):
        img_gray_all[row] = img_gray_matrix[row] + temp
        temp = img_gray_all[row]
    # print(img_gray_all)

    # 进行灰度直方图的均衡
    img_histogram = np.copy(img_martix)
    for row in range(m):
        for pix in range(n):
            img_histogram[row][pix] = round((img_gray_all[img_martix[row][pix]] * 255) / (a * b))
    # print(img_histogram)

    # 绘制直方图
    pyplot.hist(x=img_martix.flatten(), bins=400, facecolor='green')
    pyplot.show()
    pyplot.hist(x=img_histogram.flatten(), bins=400, facecolor='blue')
    pyplot.show()

    # 显示处理后的图片
    img_final = Image.fromarray(img_histogram)
    img_final.save(path_gray2)


ini = input('Input initial name:')
final = input('Input final name:')
picture_gray(ini, final)
