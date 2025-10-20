import base64

from django.core.files.base import ContentFile
from django.http import HttpResponse


def hx_trigger(trigger: str, status: int = 204) -> HttpResponse:
    response = HttpResponse(status=status)
    response["HX-Trigger"] = trigger
    return response


def base64_to_content_file(
    image_base64: str, filename: str = "image.png"
) -> ContentFile:
    return ContentFile(base64.b64decode(image_base64), name=filename)
