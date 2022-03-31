import cv2
import utils
from PIL import Image
import numpy as np
import colorsys
import random
import os

bg_files = os.listdir('resource/background')
light_files = os.listdir('resource/light')
bucket_files = os.listdir('resource/bucket2')
# target_hue = 0
OUTPUT_SIZE = (2048, 2048)
OUTPUT_PATH = 'output#4-3500-newbucket'
utils.mkdir(OUTPUT_PATH)
stored = []
for i in range(1, 3501):
    bg_idx = random.randint(0, len(bg_files)-1)
    light_idx = random.randint(0, len(light_files)-1)
    bucket_idx = random.randint(0, len(bucket_files)-1)
    if ''.join([str(bg_idx), str(light_idx), str(bucket_idx)]) in stored:
        print('repeated.')
    else:
        stored.append(''.join([str(bg_idx), str(light_idx), str(bucket_idx)]))
        bg = Image.open('resource/background/{}'.format(bg_files[bg_idx]))
        bucket = Image.open('resource/bucket2/{}'.format(bucket_files[bucket_idx]))
        light = Image.open('resource/light/{}'.format(light_files[light_idx]))
        logo = Image.open('resource/logo/kfc.png')
        bg = bg.resize(OUTPUT_SIZE)
        bucket = bucket.resize(OUTPUT_SIZE)
        light = light.resize(OUTPUT_SIZE)
        bg.paste(bucket, (0, 0), bucket)
        bg.paste(light, (0, 0), light)
        bg.paste(logo, (0, 0), logo)
        bg.save('{}/{}.png'.format(OUTPUT_PATH, i), 'PNG')
        # banner = Image.open('output#2banner/{}.png'.format(i))
        # bg_new = Image.new('RGB', (bg.width, bg.height + banner.height))
        # bg_new.paste(bg, (0, 0))
        # bg_new.paste(banner, (0, bg.height))
        # bg_new.save('{}/{}.png'.format(OUTPUT_PATH, i), 'PNG')
        print(i)
#
# bucket = Image.open('resource/bucket/warm2048.png')
#
# bucket = bucket.resize(OUTPUT_SIZE)
# bg.paste(bucket,  (0, 0), bucket)
# bg.show()
#
# image = Image.open('resource/bucket/warm2048.png')
# image.show()
# r, g, b, a = image.split()
# result_r, result_g, result_b, result_a = [], [], [], []
# # 依次对每个像素点进行处理
# for pixel_r, pixel_g, pixel_b, pixel_a in zip(r.getdata(), g.getdata(),
#                                               b.getdata(), a.getdata()):
#     # 转为 HSV 色值
#     h, s, v = colorsys.rgb_to_hsv(pixel_r / 255., pixel_b / 255., pixel_g / 255.)
#     print(h)
#     # 转回 RGB 色系
#     rgb = colorsys.hsv_to_rgb(h, s, v)
#     pixel_r, pixel_g, pixel_b = [int(x * 255.) for x in rgb]
#     # 每个像素点结果保存
#     result_r.append(pixel_r)
#     result_g.append(pixel_g)
#     result_b.append(pixel_b)
#     result_a.append(pixel_a)
#
# r.putdata(result_r)
# g.putdata(result_g)
# b.putdata(result_b)
# a.putdata(result_a)
#
# # 合并图片
# image = Image.merge('RGBA', (r, g, b, a))
# image.show()


