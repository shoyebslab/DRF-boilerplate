from rest_framework.renderers import JSONRenderer


class CustomJSONRenderer(JSONRenderer):
    """
    Standardized JSON Renderer ensuring consistent structure for all API responses.
    """
    charset = "utf-8"

    def render(self, data, accepted_media_type=None, renderer_context=None):
        if renderer_context is not None:
            response = renderer_context.get("response")
            if response and response.exception:
                return super().render(data, accepted_media_type, renderer_context)

        return super().render(data, accepted_media_type, renderer_context)
