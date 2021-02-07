from django.urls import path, re_path, include
from .views import CustomerViewSet, AccountView, TransferView
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('accounts/', AccountView.as_view()),
    path('accounts/<int:pk>/', AccountView.as_view()),
    path('transfers/', TransferView.as_view()),
    path('transfers/<int:pk>/', TransferView.as_view())
]