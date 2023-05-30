from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('adventures/', views.adventures, name='adventures'),
    path('adventures/<int:id>', views.adv_details, name='adventure'),
    path('<int:id>/booking', views.book_adv, name='booking'),
    path('<int:id>/order', views.order_page, name='order'),
    # path('order/', views.order_page),
    path('login/', views.login_page, name='login'), 
    path('signup/', views.signup_page, name='signup')
]
