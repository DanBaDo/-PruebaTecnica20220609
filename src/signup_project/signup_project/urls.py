from django.urls import path, include

from rest_framework.routers import SimpleRouter
router = SimpleRouter()

from django.contrib import admin
from profiles_api import views

#router.register(r'profiles', views.ProfilesViewSet, basename="profiles")

urlpatterns = [
    path('admin/', admin.site.urls),
    #path(r'profiles/',include(router.urls)),
    path(r'profiles/', views.GetProfiles.as_view(), { "basename": "profiles_api"}),
    path(r'profile/', views.PostProfiles.as_view(), { "basename": "profiles_api"}),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]