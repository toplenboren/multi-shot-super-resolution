from pathlib import Path
from PIL import Image
from typing import List

import rawpy
import pillow_heif
import numpy as np

RAW_EXTS = {".dng", ".arw", ".nef", ".cr2", ".cr3", ".orf", ".rw2"}

pillow_heif.register_heif_opener()

def validate_images(images: List[np.ndarray]) -> bool:
    return True

def upscale(images: List[np.ndarray]) -> np.ndarray:
    if not validate_images(images):
        raise ValueError("Invalid images")
    raise NotImplementedError("Upscaling not implemented yet")

def load_image(path: str) -> np.ndarray:
    if not Path(path).exists():
        raise ValueError(f"File does not exist: {path}")
    
    extension = Path(path).suffix.lower()
    
    try:
        if extension in RAW_EXTS:
            with rawpy.imread(path) as raw:
                return raw.postprocess()   
        image = Image.open(path).convert("RGB")
        return np.array(image)
    except Exception as err:
        raise ValueError(f"Failed to load image {path}: {err}")

def load_images_from_dir(directory: str) -> List[np.ndarray]:
    if not Path(directory).exists():
        raise ValueError(f"Directory does not exist: {directory}")
    
    images = []
    for file in Path(directory).iterdir():
        # Skip .DS_Store and other hidden files
        if file.is_file() and not file.name.startswith("."):
            images.append(load_image(file))
    
    return images

def save_image(image: np.ndarray, path: str) -> None:
    Image.fromarray(image).save(path, format="PNG")
