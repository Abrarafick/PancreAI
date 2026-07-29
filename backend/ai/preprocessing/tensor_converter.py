import torch
import numpy as np


def to_tensor(image):

    image = np.transpose(image, (2, 0, 1))

    image = torch.tensor(image, dtype=torch.float32)

    return image
