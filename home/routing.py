from django.urls import path
from .consumer import MyAsyncComsumer, MySyncComsumer
ws_patterns = [
    # path('admin/', admin.site.urls),
    path('ws/ac/', MyAsyncComsumer.as_asgi()),
    path('ws/sc/', MySyncComsumer.as_asgi()),
]
