from django.urls import path 

from .views import TestView,TeachView

urlpatterns = [
    path('TestView', Views.TestView),
    path('teachview', Views.TeachView),
]
