from django.urls import path
from . import views
app_name = 'firstpage'

urlpatterns =[
    path('',views.homepage,name='homepage'),
    path('andki/',views.andki,name='andki')
]