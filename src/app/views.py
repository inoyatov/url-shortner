from django.shortcuts import render

# Create your views here.

from rest_framework import generics, status
from rest_framework.response import Response


class URLShortnerAPIView(generics.RetrieveAPIView):
    def retrieve(self, request, *args, **kwargs):
        content = {'please move along': 'nothing to see here'}
        return Response(content, status=status.HTTP_404_NOT_FOUND)
