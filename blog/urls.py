from django.urls import path
from . import views

urlpatterns = [
    path('', views.a_view, name='a_view'),
    #path('upload/', views.upload, name='upload'),
    #path('', views.connection_test, name='connection_test'),
    #path('upload/', views.upload, name='upload'),  #test
]
