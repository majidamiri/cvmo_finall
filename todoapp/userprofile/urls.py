from django.urls import path
from .views import FreelancerListCreateAPIView, FreelancerDetailAPIView

app_name = 'freelancers'

urlpatterns = [
    path('', FreelancerListCreateAPIView.as_view(), name="list"),
    path('<int:pk>/', FreelancerDetailAPIView.as_view(), name="detail"),
]
