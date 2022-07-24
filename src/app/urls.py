from django.urls import include, path

from .views import URLShortnerAPIView


# from rest_framework.routes import DefaultRouter

# router = DefaultRouter()


urlpatterns = [
    path("", URLShortnerAPIView.as_view(), name="get_url"),
]
