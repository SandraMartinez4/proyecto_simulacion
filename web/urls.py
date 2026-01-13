from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings
from .views import index
import os

urlpatterns = [
    path('', index, name='index'),

    re_path(
        r'^html/(?P<path>.*)$',
        serve,
        {'document_root': os.path.join(settings.BASE_DIR, 'temp_html')}
    ),
]



