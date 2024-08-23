from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CourseViewSet, CourseListCreateAPIView, \
    CourseRetrieveUpdateDestroyAPIView

router = DefaultRouter()
router.register(r'courses', CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create/', CourseListCreateAPIView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseRetrieveUpdateDestroyAPIView.as_view(), name='course-retrieve-update-destroy'),
]
