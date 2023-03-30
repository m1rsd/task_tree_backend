from django.urls import re_path, path

from apps.views import index

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>', index, name='index')
]
