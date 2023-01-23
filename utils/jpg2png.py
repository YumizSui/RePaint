# -*- coding: utf-8 -*-
import sys
from PIL import Image
import os

indir=sys.argv[1]
outdir=sys.argv[2]
files = os.listdir(indir)
files = sorted([name for name in files if name.split(".")[-1] in ["png","jpg"]])
for i,val in enumerate(files):
  fname=os.path.basename(val)
  print(fname)
  fname=fname.replace('jpg','png')
  im = Image.open(f'{indir}/{val}')
  im.save(f'{outdir}/{fname}', quality=95)