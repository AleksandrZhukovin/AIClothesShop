from django.views.generic import DetailView
from django.http import JsonResponse, HttpResponse

from server.apps.catalog.models import Item
from server.apps.catalog.services.print_generator import OpenAIPrintGenerator
from server.apps.catalog.services.user_gallery_manager import UserGalleryManager


__all__ = ("ConfiguratorView",)


class ConfiguratorView(DetailView):
    model = Item
    template_name = "catalog/item_configurator.html"
    context_object_name = "item"
    pk_url_kwarg = "item_id"

    def post(self, request, *args, **kwargs):
        user_prompt = self.request.POST.get("user_prompt")
        if user_prompt:
            print_generator = OpenAIPrintGenerator(user_prompt)
            user_gallery_manager = UserGalleryManager(
                self.request.user, self.request.session
            )
            try:
                print_image = print_generator.generate()
                print_url = user_gallery_manager.save_image(print_image)
                return JsonResponse({"print_url": print_url})
            except Exception as e:
                return JsonResponse({"error": str(e)}, status=500)
        return HttpResponse(status=204)
