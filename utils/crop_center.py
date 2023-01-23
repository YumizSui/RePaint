# -*- coding: utf-8 -*-
import sys
from PIL import Image
import os

ORIGINAL_FILE_DIR = "ILSVRC2012_test/"
TRIMMED_FILE_DIR = "ILSVRC2012_test_trim/"

def crop_center(path, crop_width, crop_height):
    im = Image.open(path)
    img_width, img_height = im.size
    return im.crop(((img_width - crop_width) // 2,
                    (img_height - crop_height) // 2,
                    (img_width + crop_width) // 2,
                    (img_height + crop_height) // 2))


if __name__ == '__main__':
  if os.path.isdir(TRIMMED_FILE_DIR) == False:
    os.makedirs(TRIMMED_FILE_DIR)

  files = os.listdir(ORIGINAL_FILE_DIR)
  files = [name for name in files if name.split(".")[-1] in ["png","jpg"]]

  for i,val in enumerate(files):
    path = ORIGINAL_FILE_DIR + val
    im_trimmed = crop_center(path, 256, 256)
    fname=f'{i:05d}.png'
    im_trimmed.save(TRIMMED_FILE_DIR+fname, quality=95)
