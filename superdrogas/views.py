"""
Vue project

Vue project index built
"""

# from django.shortcuts import render
from django.http import HttpResponse


def vue(request):
    """
    vue return the Vue index
    """
    # return render(request, template_name='index.html')
    return HttpResponse('Vue project')
