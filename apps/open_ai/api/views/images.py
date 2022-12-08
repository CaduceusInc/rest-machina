import io

from django.conf import settings
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

from apps.open_ai.api.serializers import ImageSerializer, ImageFromPromptSerializer
from apps.open_ai.api.utils.images import get_image, get_image_from_url, get_image_from_file, get_image_from_base64

from apps.open_ai.client.image_generation import ImageGenerationClient

class ImageGeneratorAPIView(APIView):
    # parser_classes = (MultiPartParser, FormParser)
    serializer_class = ImageFromPromptSerializer
    permission_classes = [AllowAny,]

    def get_serializer(self, *args, **kwargs):
        return self.serializer_class(*args, **kwargs)


    def post(self, request, *args, **kwargs):
        serializer = ImageFromPromptSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        n = serializer.validated_data['n']
        size = serializer.validated_data['size']
        response_format = serializer.validated_data['response_format']
        prompt = serializer.validated_data['prompt']

        try:
            client = ImageGenerationClient(api_key=settings.OPENAI_API_KEY)
            image = client.generate_image(prompt, n)
            return Response(
                {
                    "status": "success",
                    "data": {
                        "generated_data": image
                    },
                    "status_code": status.HTTP_200_OK,
                    "message": "Image generated successfully"
                },
                status=status.HTTP_200_OK
            )

        except Exception as e:
            return Response(
                {
                    "status": "error",
                    "data": {
                        "image": None
                    },
                    "error": str(e),
                    "status_code": status.HTTP_400_BAD_REQUEST,
                    "message": "Image generation failed"
                },
                status=status.HTTP_400_BAD_REQUEST
            )



