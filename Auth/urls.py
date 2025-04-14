from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# simple view for homepage
def home(request):
    return HttpResponse("Welcome to the homepage!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
]
