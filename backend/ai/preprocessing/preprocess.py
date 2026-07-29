import cv2
import numpy as np

from .config import IMAGE_SIZE


def resize_image(image):
    return cv2.resize(image, IMAGE_SIZE)


def normalize_image(image):
    image = image.astype(np.float32) / 255.0
    return image


def preprocess(image):
    image = resize_image(image)
    image = normalize_image(image)
    return image
