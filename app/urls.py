from django.urls import path
from .views import HomeView, FormIsSubmitedView

urlpatterns = [
    path('', HomeView.as_view(), name='application'),
    path('thanks/', FormIsSubmitedView.as_view(), name='thanks')
]
