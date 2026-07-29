import cv2


def remove_noise(image):
    """
    Remove image noise using Gaussian Blur.
    """
    return cv2.GaussianBlur(image, (5, 5), 0)
