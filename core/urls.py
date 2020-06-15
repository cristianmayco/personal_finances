from django.urls import path

from .views import IndexView, EditView, BillDeleteView, BillCreateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('bill/<int:pk>', EditView.as_view(), name='edit'),
    path('bill/delete/<int:pk>', BillDeleteView.as_view(), name='delete'),
    path('bill/new', BillCreateView.as_view(), name='create')
]
