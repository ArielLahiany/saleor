from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse

from .manager import get_plugins_manager


def handle_plugin_webhook(request: WSGIRequest, plugin_id: str) -> HttpResponse:
    manager = get_plugins_manager()
    return manager.webhook_endpoint_without_channel(request, plugin_id)


def handle_global_plugin_webhook(request: WSGIRequest, plugin_id: str) -> HttpResponse:
    manager = get_plugins_manager()
    return manager.webhook(request, plugin_id, channel_slug=None)


def handle_plugin_per_channel_webhook(
    request: WSGIRequest, plugin_id: str, channel_slug: str
) -> HttpResponse:
    manager = get_plugins_manager()
    return manager.webhook(request, plugin_id, channel_slug=channel_slug)
