from django.urls import path
from .views import *

urlpatterns = [
    path('',home, name='home'),
    path('post/<int:id>/',detail, name='detail'),
    path('create/',create, name='create'),
    path('post/<int:id>/update/',update, name='update'),
    path('post/<int:id>/delete/',delete, name='delete'),
]