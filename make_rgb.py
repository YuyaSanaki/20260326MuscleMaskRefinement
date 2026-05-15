from PIL import Image
import numpy as np
import os

def create_rgb_composite(file_path):
    img = Image.open(file_path)
    channels = []
    for i in range(4):
        img.seek(i)
        ch_data = np.array(img).astype(float)
        # Normalize each channel to 0-255
        ch_min, ch_max = ch_data.min(), ch_data.max()
        if ch_max > ch_min:
            ch_data = (ch_data - ch_min) / (ch_max - ch_min) * 255
        channels.append(ch_data)
    
    # Mapping (0-indexed):
    # Ch1 (idx 0) -> Magenta (R+B)
    # Ch2 (idx 1) -> Green (G)
    # Ch3 (idx 2) -> Blue (B)
    # Ch4 (idx 3) -> Red (R)
    
    h, w = channels[0].shape
    rgb = np.zeros((h, w, 3), dtype=np.float32)
    
    # Red = Ch4 + Ch1
    rgb[..., 0] = channels[3] + channels[0]
    # Green = Ch2
    rgb[..., 1] = channels[1]
    # Blue = Ch3 + Ch1
    rgb[..., 2] = channels[2] + channels[0]
    
    # Clip and convert to uint8
    rgb = np.clip(rgb, 0, 255).astype(np.uint8)
    
    out_name = file_path.replace('.tif', '_rgb.png')
    Image.fromarray(rgb).save(out_name)
    print(f"Created {out_name} with new mapping")
    return out_name

if __name__ == "__main__":
    files = ['TG_Sol.tif', 'WT_Sol.tif', 'WT_TA.tif']
    for f in files:
        if os.path.exists(f):
            create_rgb_composite(f)
