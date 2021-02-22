from django.urls import path
from shrtnr import views

urlpatterns = [
    path('', views.shrtnr),
    path('<str:shrt>', views.shrtnr_record)
]
