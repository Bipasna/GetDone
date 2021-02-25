from django.urls import path

from.import views


urlpatterns=[
    path('',views.index, name='index'),
    path('settings',views.settings,name='setting'),
    path('about',views.about,name='about')

]