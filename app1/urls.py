from django.urls import path
from .views import *

urlpatterns = [
    path('get_data/', GetUserData.as_view(), name="get_data"),
    path('create_data/', CreateUserData.as_view(), name="create_data"),
    path('update_data/<int:pk>', EditUserData.as_view(), name="update_data"),
    path('delete_data/<int:pk>', DeleteUserData.as_view(), name="delete_data")
]