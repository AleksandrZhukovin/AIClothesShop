import base64
import os
import openai

from django.core.files.base import ContentFile

from server.apps.user.models import GalleryImage


class OpenAIPrintGenerator:
    def __init__(self, user_prompt, user, session, model="gpt-4o"):
        self.user_prompt = user_prompt
        self.user = user
        self.session = session
        self.print_prompt = None
        self.model = model
        self.api_key = os.environ.get("OPENAI_API_KEY")
        if not self.api_key:
            raise EnvironmentError("OPENAI_API_KEY environment variable not set.")

    def get_print_prompt(self):
        if not self.user_prompt:
            raise ValueError("Cannot generate print with an empty user prompt")
        context_prompt = """Generate a high-resolution t-shirt print design.
               The design must be centered on a transparent background, with no model, no t-shirt, and no background.
               Do not include people or clothing. The image should resemble a sticker or decal.
               Prompt:
            """
        self.print_prompt = " ".join((context_prompt, self.user_prompt))
        return self.print_prompt

    def unauthenticated_user_save(self, image_data):
        return GalleryImage.unauthenticated_user_save(image_data, self.session)

    def authenticated_user_save(self, image_data):
        if image_data:
            image_base64 = image_data[0]
            image_bytes = base64.b64decode(image_base64)
            image_file = ContentFile(image_bytes)
            gallery_image = GalleryImage.objects.create(user=self.user)
            gallery_image.image.save("print.png", image_file, save=True)
            return gallery_image.image.url

    def generate(self):
        openai.api_key = self.api_key
        self.get_print_prompt()

        try:
            response = openai.responses.create(
                model=self.model,
                input=self.print_prompt,
                tools=[{"type": "image_generation"}],
            )
            image_data = [
                output.result
                for output in response.output
                if output.type == "image_generation_call"
            ]
            if self.user.is_authenticated:
                return self.authenticated_user_save(image_data)
            else:
                return self.unauthenticated_user_save(image_data)
        except Exception as e:
            raise RuntimeError(f"OpenAI image generation failed: {e}")
