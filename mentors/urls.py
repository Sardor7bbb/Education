from django.urls import path
from .views import RegisterCreateAPIView, MentorDetailView

app_name = 'mentors'

urlpatterns = [
    path('bio/', RegisterCreateAPIView.as_view(), name='bio'),
    path('profile/', MentorDetailView.as_view(), name='profile'),
]
