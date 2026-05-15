from PIL import Image
import numpy as np
import os

files = ['TG_Sol.tif', 'WT_Sol.tif', 'WT_TA.tif']
for f in files:
    if os.path.exists(f):
        img = Image.open(f)
        data = np.array(img)
        print(f"{f}: {data.shape}, Mode: {img.mode}")
        # If multi-page TIFF, check frame count
        try:
            img.seek(1)
            print(f"{f} is multi-page")
        except EOFError:
            print(f"{f} is single-page")
