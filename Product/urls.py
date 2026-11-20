from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListCreateProduct.as_view(), name="Create-and-List"),
    path('product/<int:pk>', views.DetailUpdateDelete.as_view(), name='ProductUpdateDelete'),
]
