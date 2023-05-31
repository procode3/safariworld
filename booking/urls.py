from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('adventures/', views.adventures, name='adventures'),
    path('adventures/<str:id>', views.adv_details, name='adventure'),
    path('<str:id>/booking', views.book_adv, name='booking'),
    path('<str:id>/order', views.order_page, name='order'),
    # path('order/', views.order_page),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),  
    path('signup/', views.signup_page, name='signup')
]
