import torch.nn as nn
from torchvision import models

from .train_config import NUM_CLASSES


def get_densenet121():

    model = models.densenet121(weights=models.DenseNet121_Weights.DEFAULT)

    in_features = model.classifier.in_features

    model.classifier = nn.Linear(in_features, NUM_CLASSES)

    return model
