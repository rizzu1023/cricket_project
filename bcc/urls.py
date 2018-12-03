from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='bcc-home'),
    path('about/',views.about, name='bcc-about'),
]