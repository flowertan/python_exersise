# coding=utf-8
#
# @Author  : flower
# @Version : 1.0
# @Time    : 2019/7/28 20:31
# @file    : image.py
# @desc    : pillow库的使用
#

from PIL import Image, ImageFilter


# 生成缩略图
image = Image.open('maomi.jpeg')
size = 128, 128
image.thumbnail(size)
image.show()

# 旋转与翻转
image = Image.open('maomi.jpeg')
# image.save('maomi.png')
# im = Image.open('maomi.png')
image.rotate(180).show()
image.transpose(Image.FLIP_LEFT_RIGHT).show()

# 操作像素
for x in range(80, 310):
    for y in range(20, 360):
        image.putpixel((x, y), (128, 128, 128))

image.show()

# 滤镜效果
image = Image.open('maomi.jpeg')
size = 256, 256
image.thumbnail(size)
image.filter(ImageFilter.CONTOUR).show()
