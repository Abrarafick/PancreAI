import torch.nn as nn
from torchvision import models

from .train_config import NUM_CLASSES


def get_resnet50():

    model = models.resnet50(weights=models.ResNet50_Weights.DEFAULT)

    in_features = model.fc.in_features

    model.fc = nn.Linear(in_features, NUM_CLASSES)

    return model
