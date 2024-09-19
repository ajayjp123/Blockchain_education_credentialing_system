from django.urls import path
from .views import store_credential, verify_credential

urlpatterns = [
    path('store_credential/', store_credential, name='store_credential'),
    path('verify_credential/', verify_credential, name='verify_credential'),
]
