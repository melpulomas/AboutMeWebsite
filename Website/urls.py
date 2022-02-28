# Best to have urls.py in own specific application.
# The entire project urls.py will also be edited to reflect the changes made here.
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index")
]
