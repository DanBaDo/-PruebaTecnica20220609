from rest_framework import generics, permissions, viewsets

from profiles_api.models import Profile
from profiles_api.serializers import PostProfileSerializer, GetProfileSerializer


# Create your views here.

class PostProfiles(generics.CreateAPIView):
    """
    Profile creation
    """
    serializer_class = PostProfileSerializer
    permission_classes = [permissions.AllowAny]

class GetProfiles(generics.ListAPIView):
    """
    Profiles list
    """
    queryset = Profile.objects.all()
    serializer_class = GetProfileSerializer
    permission_classes = [permissions.IsAdminUser]

class ProfilesViewSet(viewsets.ViewSet):
    def create(self, request):
        queryset = Profile.objects.all()
        serializer_class = PostProfileSerializer
        permission_classes = [permissions.AllowAny]
    def list(self, request):
        queryset = Profile.objects.all()
        serializer_class = GetProfileSerializer
        permission_classes = [permissions.IsAdminUser]