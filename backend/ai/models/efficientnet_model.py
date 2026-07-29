import torch.nn as nn
from torchvision import models

from .train_config import NUM_CLASSES


def get_efficientnet_b0():

    model = models.efficientnet_b0(
        weights=models.EfficientNet_B0_Weights.DEFAULT
    )

    in_features = model.classifier[1].in_features

    model.classifier[1] = nn.Linear(in_features, NUM_CLASSES)

    return model
