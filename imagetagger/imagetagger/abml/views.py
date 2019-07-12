from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse

# Create your views here.

@login_required
def index(request):
    return TemplateResponse(request, 'abml/index.html', {
    })
