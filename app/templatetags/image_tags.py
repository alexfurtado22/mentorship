# app/templatetags/image_tags.py
import os

from django import template
from django.conf import settings
from PIL import Image

register = template.Library()


@register.filter
def image_placeholder_size(image_url):
    try:
        # Remove MEDIA_URL prefix if present
        relative_path = image_url.replace(settings.MEDIA_URL, "")
        img_path = os.path.join(settings.MEDIA_ROOT, relative_path)

        img = Image.open(img_path)
        width, height = img.size

        return f"https://placehold.co/{width}x{height}"
    except Exception as e:
        print(f"❌ image_placeholder_size error: {e}")
        return "https://placehold.co/400x300"
