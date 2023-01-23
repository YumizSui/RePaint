
import torch
import pandas as pd
import os
from glob import glob
from tqdm import tqdm
import torchvision.transforms.functional as TF
from PIL import Image
import lpips

loss_fn_alex = lpips.LPIPS(net='alex')
loss_fn_alex.eval()

def get_lpips(original_path, inpaint_path):
    img_original = Image.open(original_path)
    img_original = (TF.to_tensor(img_original) - 0.5) * 2
    img_original.unsqueeze(0)

    img_inpaint = Image.open(inpaint_path)
    img_inpaint = (TF.to_tensor(img_inpaint) - 0.5) * 2
    img_inpaint.unsqueeze(0)

    d = loss_fn_alex(img_original, img_inpaint).item()
    # print("Perceptual loss",d)
    return d

workdir='/home/kfurui/dfurui/workspace/clones/RePaint/log/myresnet/'
exps = os.listdir(workdir)
all_scores = {}
for exp in exps:
    scores=[]
    for idx in tqdm(range(100)):
        original_path = f'{workdir}/{exp}/gt/{idx:05d}.png'
        inpaint_path = f'{workdir}/{exp}/inpainted/{idx:05d}.png'
        score = get_lpips(original_path,inpaint_path)
        scores+=[score]
    all_scores[exp]=scores
all_scores = pd.DataFrame(all_scores)
print(all_scores.mean())

# all_scores.to_csv('results/result.csv')