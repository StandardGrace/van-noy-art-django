from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('student/add/', views.add_student, name='add_student'),
    path('students/', views.student_list, name='student_list'),
    path('products/', views.product_list, name='product_list'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('gallery/', views.gallery, name='gallery'),
    path('upload/', views.upload_piece, name='upload_piece'),
    path('sales/', views.sales, name='sales'),
]