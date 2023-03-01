from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.
@api_view()
def Book_list(request):
    return Response("everything is awesome",
                    status=status.HTTP_200_OK)