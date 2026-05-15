import os
from PIL import Image

def get_tiff_info(file_path):
    try:
        with Image.open(file_path) as img:
            return {
                "file": os.path.basename(file_path),
                "size": img.size,
                "mode": img.mode,
                "format": img.format
            }
    except Exception as e:
        return {"file": os.path.basename(file_path), "error": str(e)}

files = [f for f in os.listdir('.') if f.endswith(('.tif', '.tiff'))]
infos = [get_tiff_info(f) for f in files]

for info in infos:
    print(info)
