import os
import openai

from django.core.files.base import ContentFile

from server.apps.core.utils import base64_to_content_file


class OpenAIPrintGenerator:
    PRINT_CONTEXT_PROMPT = """Generate a high-resolution t-shirt print design.
               The design must be centered on a transparent background, with no model, no t-shirt, and no background.
               Do not include people or clothing. The image should resemble a sticker or decal.
               Prompt:
            """
    DEFAULT_PRINT_FILENAME = "print.png"

    def __init__(self, user_prompt, model="gpt-4o"):
        self.user_prompt = user_prompt
        self.model = model
        self.api_key = os.environ["OPENAI_API_KEY"]

    def generate(self) -> ContentFile:
        prompt = f"{self.PRINT_CONTEXT_PROMPT} {self.user_prompt}"
        response = openai.responses.create(
            model=self.model,
            input=prompt,
            tools=[{"type": "image_generation"}],
        )
        image_base64 = next(
            output.result
            for output in response.output
            if output.type == "image_generation_call"
        )
        return base64_to_content_file(image_base64, self.DEFAULT_PRINT_FILENAME)
