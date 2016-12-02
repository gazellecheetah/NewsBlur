from django.conf.urls import url
from apps.push import views

urlpatterns = [
    url(r'^(?P<push_id>\d+)/?$', views.push_callback, name='push-callback'),
]
