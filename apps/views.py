from django.shortcuts import render


def index(request, pk=None):
    return render(request, 'apps/index.html')
