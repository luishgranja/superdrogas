"""
Project views

Vue project built
"""

from django.shortcuts import render


def index(request):
    """
    index return the Vue index
    """
    return render(request, template_name='index.html')
