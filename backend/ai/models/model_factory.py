from .resnet_model import get_resnet50
from .densenet_model import get_densenet121
from .efficientnet_model import get_efficientnet_b0


def load_model(model_name):

    if model_name == "resnet50":
        return get_resnet50()

    elif model_name == "densenet121":
        return get_densenet121()

    elif model_name == "efficientnet_b0":
        return get_efficientnet_b0()

    else:
        raise ValueError(f"Unsupported model: {model_name}")
    