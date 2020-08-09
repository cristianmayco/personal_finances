from django.urls import path

from .views import HomeView, EditView, BillDeleteView, BillCreateView, BillDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('bill/<int:pk>', EditView.as_view(), name='edit'),
    path('bill/delete/<int:pk>', BillDeleteView.as_view(), name='delete'),
    path('bill/new', BillCreateView.as_view(), name='create'),
    path('bill/detail/<int:pk>', BillDetailView.as_view(), name='detail')
]
