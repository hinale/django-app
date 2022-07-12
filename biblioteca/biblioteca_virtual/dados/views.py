from django.shortcuts import render
from rest_framework import viewsets
from .models import Cliente
from .serializers import ClienteSerializer
from django.views.decorators.cache import cache_page

# Create your views here.


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


# @cache_page(60)
def home(request):
    clientes = Cliente.objects.all()
    return render(request, 'dados/index.html', {'clientes': clientes})
