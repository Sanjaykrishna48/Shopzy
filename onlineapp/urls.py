from . import views
from django.urls import path
# from django import views
urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('adminhome/',views.adminhome),
    path('adminhome/addcategory/',views.addcategory),
    path('adminhome/addsubcategory/',views.addsubcategory),
    path('adminhome/addbrand/',views.addbrand),
    path('adminhome/addproduct/',views.addproduct),
    path('registration/',views.registration),
    path('login/',views.login),
    path('userhome/',views.userhome),
    path('userhome/buyproduct/',views.buyproduct),




]
