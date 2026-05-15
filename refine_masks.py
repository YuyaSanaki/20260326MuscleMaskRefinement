import napari
import os
from PIL import Image
import numpy as np

def load_data():
    print(f"Starting napari version: {napari.__version__}")
    viewer = napari.Viewer()
    
    # Custom color map (Shifted by +1 to make Label 0 transparent)
    # We map your 0-7 classes to 1-8 in the viewer.
    custom_colors = {
        1: [100/255, 200/255, 210/255, 1.0], # Uncertain (was 0)
        2: [230/255, 230/255, 230/255, 1.0], # Background (was 1)
        3: [210/255, 130/255, 210/255, 1.0], # TypeIIB (was 2)
        4: [130/255, 190/255, 130/255, 1.0], # TypeI (was 3)
        5: [70/255, 130/255, 180/255, 1.0],  # Membrane (was 4)
        6: [230/255, 115/255, 115/255, 1.0], # TypeIIA (was 5)
        7: [50/255, 50/255, 50/255, 1.0],    # TypeIIX (was 6)
        8: [220/255, 190/255, 80/255, 1.0]    # Vessel (was 7)
    }

    # Define pairs of (raw_image, mask)
    pairs = [
        ('TG_Sol_rgb.png', 'TG_Sol_Simple Segmentation.tiff'),
        ('WT_Sol_rgb.png', 'WT_Sol_Simple Segmentation.tiff'),
        ('WT_TA_rgb.png', 'WT_TA_Simple Segmentation.tiff')
    ]
    
    for img_path, mask_path in pairs:
        if os.path.exists(img_path) and os.path.exists(mask_path):
            img = np.array(Image.open(img_path))
            viewer.add_image(img, name=img_path)
            
            # Load mask and SHIFT by +1
            mask = np.array(Image.open(mask_path))
            shifted_mask = mask + 1
            
            layer = viewer.add_labels(shifted_mask, name=mask_path)
            layer.color = custom_colors
            
    # Add a message to help the user
    print("\n--- SHIFTED LABEL GUIDE ---")
    print("Labels are shifted by +1 for visibility in Napari:")
    print("1: Uncertain, 2: Background, 3: TypeIIB, 4: TypeI, 5: Membrane, 6: TypeIIA, 7: TypeIIX, 8: Vessel")
    print("IMPORTANT: When saving, the values will be 1-8. I will provide a script to shift them back to 0-7.")
    
    napari.run()

if __name__ == "__main__":
    load_data()
