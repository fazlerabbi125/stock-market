"""stock URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import *
from django.views.generic import TemplateView
app_name="janata"

from csv import DictReader
from django.http import HttpResponse
from django.utils.dateparse import parse_date
def load(request):
    BASE_DIR = Path(__file__).resolve().parent.parent
    file=open(f'{BASE_DIR}/janata_stock.csv')
    c=DictReader(file)
    for row in c:
        Stock.objects.create(trade_code=row['trade_code'],date=parse_date(row['date']),high=row['high'],
        low=row['low'],open=row['open'],close=row['close'],volume=row['volume'])

    return HttpResponse('success')
urlpatterns = [
    path('', StockListView.as_view(), name='home'),
    path('load/', load, ),
    path('json-home/', jsonlist, name='jsonView'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('stock/add/', addStock, name='add'),
    path('stock/<int:pk>/edit/', updateStock, name='edit'),
    path('stock/<int:pk>/delete/', StockDeleteView.as_view(), name='delete'),

]
