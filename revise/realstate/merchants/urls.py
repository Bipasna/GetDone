from django.urls import path
from . import views

urlpatterns=[
    path('',views.index, name="merchantList"),
 
    path('search', views.search, name="merchantSearch"),
    path('<int:merchant>',views.profile, name="merchantProfile")
]