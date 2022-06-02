from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UserCreateView,CustomLoginView

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
