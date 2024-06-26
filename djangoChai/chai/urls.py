from django.urls import path
from . import views
urlpatterns = [
    path('',views.all_chai, name= "All Chai"),
    # path('order/',views.order, name= "All Order"),
 ]
