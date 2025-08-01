from django.http import HttpResponse


def hx_trigger(trigger, status=204):
    response = HttpResponse(status=status)
    response["HX-Trigger"] = trigger
    return response
