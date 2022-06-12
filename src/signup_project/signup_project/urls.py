from django.urls import path, include

from django.contrib import admin
from profiles_api.urls import urlpatterns as profiles_api_urls

#router.register(r'profiles', views.ProfilesViewSet, basename="profiles")

urlpatterns = [
    path('admin/', admin.site.urls),
    #path(r'profiles/',include(router.urls)),
    #path(r'profiles/', views.GetProfiles.as_view(), { "basename": "profiles_api"}),
    #path(r'profile/', views.PostProfiles.as_view(), { "basename": "profiles_api"}),
    path(r'',include(profiles_api_urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]