import cv2
import pydicom
import numpy as np


def load_image(image_path):
    image = cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError(f"Image not found: {image_path}")

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image


def load_dicom(dicom_path):
    dicom = pydicom.dcmread(dicom_path)
    image = dicom.pixel_array.astype(np.float32)
    return image
