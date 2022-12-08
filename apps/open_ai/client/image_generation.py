from .base import BaseClient
from django.conf import settings
import openai


class ImageGenerationClient():

    def __init__(self, api_key=None, **kwargs):
        self.api_key = api_key
        self._base_url = "https://api.openai.com/v1/"

    def _generate_image(self, **kwargs):
        url = f"{self._base_url}images/generations"
        openai.api_key = self.api_key
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        # data = {
        #     "prompt": prompt,
        #     "n": kwargs.get("n", 1),
        #     "size": kwargs.get("size", 256),
        #     "response_format": kwargs.get("response_format", "png"),
        # }
        return openai.Image.create(**kwargs)

    def generate_image(self, prompt, n, **kwargs):
        """
        Generate an image from a prompt
        :param prompt: The prompt to use for image generation
        :param n: The number of images to generate
        :param size: The size of the image to generate
        :param response_format: The format of the image to generate
        :param kwargs: Additional arguments to pass to the API
            :opional: 'user_id': The user ID to use for the request

        :return: The image generated
        """

        return self._generate_image(prompt=prompt, n=n, **kwargs)

