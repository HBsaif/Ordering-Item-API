from rest_framework import routers
from . import views
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('get_items/', views.get_item),
    path('add_item/', views.add_item),
    path('items/<int:id>', views.item_details),
    path('add_charity/', views.register_new_charity),
    path('add_user/', views.register_new_user),
    path('login_charity/', views.login_new_charity),
    path('login_user/', views.login_new_user),
    path('get_all_charities/', views.get_all_charities),
    path('get_all_items_by_email/', views.get_all_items_by_email),
    path('order_item/', views.order_item),
    path('', include(router.urls)),
]
