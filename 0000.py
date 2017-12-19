# -*- coding: utf-8
# !/usr/bin/env python

from PIL import Image, ImageDraw, ImageFont


def draw():

    img = Image.open('0000-icon.jpeg')
    # font = ImageFont.truetype('Arial.ttf',36)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('Ubuntu-L.ttf',size=32)
    draw.text((150, 15), '7', font=font, fill=(255,23,140))
    img.show()


if __name__ == '__main__':
    draw()