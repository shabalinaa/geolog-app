from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from app.models import CommonData


def index(request):
    template = 'app/index.html'
    latest_date_list = CommonData.objects.order_by('-id')[:5]
    context = {'latest_date_list': latest_date_list}
    return render(request, template, context)