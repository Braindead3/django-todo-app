from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls'), name='todo'),
    path('user/', include('users.urls'), name='users'),
]
