from django.urls import path
from .views import v_signup
urlpatterns = [
    path('signup', v_signup)
]