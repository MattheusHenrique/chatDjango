from django.contrib import admin
from django.urls import path
from django.conf.urls import include


from chat import views

urlpatterns = [
    path('chat/', include('chat.urls')),
    path('admin/', admin.site.urls),
]
