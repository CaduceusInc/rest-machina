import base64

import requests


def get_image_from_base64(image):
    """
    Get an image from a base64 encoded string
    :param image: The base64 encoded string
    :return: The image
    """
    return get_image(image, "base64")


def get_image_from_file(image):
    """
    Get an image from a file
    :param image: The file
    :return: The image
    """
    return get_image(image, "file")


def get_image_from_url(image):
    """
    Get an image from a URL
    :param image: The URL
    :return: The image
    """
    return get_image(image, "url")


def get_image(image, image_type):
    """
    Get an image from a URL, file, or base64 encoded string
    :param image: The image
    :param image_type: The type of image
    :return: The image
    """
    if image_type == "url":
        image = requests.get(image).content
    elif image_type == "file":
        image = image.read()
    elif image_type == "base64":
        image = base64.b64decode(image)
    return image
