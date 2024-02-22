from django.urls import path
from jinjaAPP import views

urlpatterns = [
    path('',views.home,name='my_home'),
    path('about/',views.aboutus,name='my_about'),
    path('contact/', views.contact, name='my_contact'),
    path('gallery/',views.gallery,name ='my_gallery')
]