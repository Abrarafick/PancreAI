from .noise_removal import remove_noise
from .contrast import enhance_contrast
from .preprocess import preprocess
from .tensor_converter import to_tensor


def process_image(image):

    image = remove_noise(image)

    image = enhance_contrast(image)

    image = preprocess(image)

    image = to_tensor(image)

    return image
