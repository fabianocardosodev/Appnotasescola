from django.urls import path  

from . import views

app_name = "principal"

urlpatterns = [ 
        path('', views.HomePageView.as_view(), name='home'),
        path('', views.HomePageView.as_view(), name='comunicados'),
        
              
]