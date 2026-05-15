import napari
import os
from PIL import Image
import numpy as np
from qtpy.QtWidgets import QFileDialog

# Custom color map (Shifted by +1 to make Label 0 transparent)
CUSTOM_COLORS = {
    1: [100/255, 200/255, 210/255, 1.0], # Uncertain
    2: [230/255, 230/255, 230/255, 1.0], # Background
    3: [210/255, 130/255, 210/255, 1.0], # TypeIIB
    4: [130/255, 190/255, 130/255, 1.0], # TypeI
    5: [70/255, 130/255, 180/255, 1.0],  # Membrane
    6: [230/255, 115/255, 115/255, 1.0], # TypeIIA
    7: [50/255, 50/255, 50/255, 1.0],    # TypeIIX
    8: [220/255, 190/255, 80/255, 1.0]    # Vessel
}

def load_image_and_mask(viewer, img_path):
    """Helper to load one image and its corresponding mask."""
    # 1. Load Raw Image (check if it's the RGB or the TIF)
    img_name = os.path.basename(img_path)
    img = np.array(Image.open(img_path))
    viewer.add_image(img, name=img_name)
    
    # 2. Look for the mask
    # Logic: if image is "Name.tif" or "Name_rgb.png", look for "Name_Simple Segmentation.tiff"
    base_name = img_name.replace('_rgb.png', '').replace('.tif', '')
    mask_name = f"{base_name}_Simple Segmentation.tiff"
    mask_path = os.path.join(os.path.dirname(img_path), mask_name)
    
    if os.path.exists(mask_path):
        mask = np.array(Image.open(mask_path))
        shifted_mask = mask + 1
        layer = viewer.add_labels(shifted_mask, name=mask_name)
        layer.color = CUSTOM_COLORS
        print(f"Loaded mask: {mask_name}")
    else:
        print(f"Warning: Mask not found at {mask_path}")

def main():
    viewer = napari.Viewer()
    
    # Open File Dialog
    print("Opening file dialog...")
    files, _ = QFileDialog.getOpenFileNames(
        None, "Select Raw Images or RGB Composites", "", "Images (*.tif *.tiff *.png *.jpg)"
    )
    
    if files:
        for f in files:
            load_image_and_mask(viewer, f)
    else:
        print("No files selected.")

    napari.run()

if __name__ == "__main__":
    main()
