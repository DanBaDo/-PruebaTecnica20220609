from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ProfilesView, ProfilesAddressesValidation

urlpatterns = [
    path('profiles/', ProfilesView.as_view()),
    path('profiles/<int:pk>/', ProfilesView.as_view()),
    path('profiles/validate/<str:jwt>', ProfilesAddressesValidation.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)