from django.urls import path
from app1.views import *
app_name='something'

urlpatterns=[
    path('Jinja_print/',Jinja_print,name='Jinja_print'),
]