from django.urls import path
from . import views
from django.conf.urls import url, include
from blog import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.a_view, name='a_view'),
    #path('upload/', views.upload, name='upload'),
    #path('', views.connection_test, name='connection_test'),
    #path('upload/', views.upload, name='upload'),  #test
    path('blog/', views.snippet_list),
    path('blog/<int:pk>/', views.snippet_detail),

]
