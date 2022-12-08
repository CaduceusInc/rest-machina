from django.urls import path

from apps.open_ai.api.views.images import ImageGeneratorAPIView

urlpatterns = [
    path("image-generator/", ImageGeneratorAPIView.as_view(), name="image-generator"),
]
