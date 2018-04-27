from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint

def product_list(request):
    return render(request,
                  'konfigurator/product/list.html')

def product_busy(request):
    return render(request,'konfigurator/product/busy.html')
