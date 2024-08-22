from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signup, user_login, custom_logout_view, subtract_payment_view, subtract_payment_view, add_loan_view, add_repayment_view
from django.views.generic import TemplateView
from . import views
urlpatterns = [
    path('', views.home, name='home'),
path('rental_record/<int:pk>/', views.rental_record_detail, name='rental_record_detail'),
path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
path('logout/', custom_logout_view, name='logout'),
    path('logged_out/', TemplateView.as_view(template_name='logged_out.html'), name='logged_out'),
path('subtract_payment/<int:pk>/', subtract_payment_view, name='subtract_payment'),
path('payment_success/<int:pk>/', TemplateView.as_view(template_name='payment_success.html'), name='payment_success'),
path('add_loan/<int:pk>/', add_loan_view, name='add_loan'),
    path('add_repayment/<int:pk>/', add_repayment_view, name='add_repayment'),

]