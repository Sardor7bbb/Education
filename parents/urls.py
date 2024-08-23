from django.urls import path
from .views import ParentCreateView, ParentUpdateView, ParentChildrenListView

app_name = 'parents'

urlpatterns = [
    path('create/', ParentCreateView.as_view(), name='children-create'),
    path('update/<int:pk>/', ParentUpdateView.as_view(), name='parent-update'),
    path('list/', ParentChildrenListView.as_view(), name='course-list'),
]
