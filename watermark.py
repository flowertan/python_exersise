# coding=utf-8
#
# @Author  : flower
# @Version : 1.0
# @Time    : 2018/8/27 18:30
# @file    : watermark.py
# @desc    : digital watermark simple method
#

from PIL import Image

info = 'learn python with crossin'
im_rgb = []
key_words = []

def get_pix(file_name):
    im = Image.open(file_name)
    rgb_im = im.convert('RGB')
    # print(im.width)
    for w in range(0, im.width):
        for h in range(0, im.height):
            r, g, b = rgb_im.getpixel((w, h))
            r = bin(r // 2 * 2)
            im_rgb.append(r[2:])
            g = bin(g // 2 * 2)
            im_rgb.append(g[2:])
            b = bin(b // 2 * 2)
            im_rgb.append(b[2:])
    # print(im_rgb)
    return im.width, im.height


def process_info():
    for i in info:
        info_bin = (bin(ord(i))[2:]).zfill(8);
        for s in info_bin:
            key_words.append(s)
        print(info_bin)
    length = len(key_words)
    for i in range(0, len(im_rgb)):
        temp = list(im_rgb[i])
        temp[-1] = key_words[i % length]
        # print(temp)
        temp_str = ''.join(temp)
        # print(temp_str)
        im_rgb[i] = temp_str
    print(im_rgb[2])
    # print(int(im_rgb[len(im_rgb) - 1], 2))

def save_pic(w, h):
    # w = 1184
    # h = 472
    
    im = Image.new("RGB", (w, h))
    index = 0
    for i in range(0, w):
        for j in range(0, h):
            im.putpixel((i, j), (int(im_rgb[index], 2), int(im_rgb[index + 1], 2), int(im_rgb[index + 2], 2)))
            index+=3
    im.save('result.png')

def side_info(file_name):
    w, h = get_pix(file_name)
    process_info()
    save_pic(w, h)

def get_info(file_name):
    im = Image.open(file_name)
    rgb_im = im.convert('RGB')
    key_info = []
    for w in range(0, im.width):
        for h in range(0, im.height):
            r, g, b = rgb_im.getpixel((w, h))
            key_info.append(bin(r)[2:][-1])
            key_info.append(bin(g)[2:][-1])
            key_info.append(bin(b)[2:][-1])
    temp = ['0', '0', '0', '0', '0', '0', '0', '0', '0']
    index = 0
    s = []
    for i in range(0, len(key_words) + 1):
        temp[index] = key_info[i]
        if index % 8 == 0:
            index = 0
            # print(temp)
            # print(''.join(temp[0:8]))
            s.append(chr(int(''.join(temp[0:8]), 2)))
            # print(s)
        index += 1
    print(''.join(s[1:]))





def main():
    input_file_name = 'test.png'
    side_info(input_file_name)
    input_file_name = 'result.png'
    get_info(input_file_name)

if __name__ == '__main__':
    main()