from PIL import Image, ImageEnhance, ImageFilter
import os

path = 'D:/insta/instaIN'
pathOut = 'D:/insta/instaOUT'
pathDel = 'D:/insta/delete'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit_name = int(input("Enter whihc filter set you want: \n 1. purple skies \n 2. auttumn vibes \n 3. day dream filter \n 4. strawberry skies \n "))

    edit_s = img.filter(ImageFilter.SHARPEN).rotate(-90)
    """"
    for strawberry skies
    highlights = -30
    shadow = +50
    contrast = -12
    saturation = -40
    warmth = +59
    tint = +30
    sharpness = +40
    
    """
    edit_ss = ImageEnhance.Contrast(edit_s).enhance(0.88)
    edit_sss = edit_ss

