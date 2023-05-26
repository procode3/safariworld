from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('adventures/', views.adventures),
    path('adventures/<int:id>', views.adv_details),
    path('<int:id>/booking', views.book_adv),
    path('<int:id>/order', views.order_page),
    # path('order/', views.order_page),
    path('login/', views.login)
]
