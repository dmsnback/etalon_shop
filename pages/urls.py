from django.urls import path

from . import views

app_name = 'pages'


urlpatterns = [
    path('about/', views.about, name='about'),
    path('contacts/', views.contact, name='contacts'),
]
