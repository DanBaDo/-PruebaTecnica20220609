from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from profiles_api.models import Profile
from profiles_api.serializers import PostProfileSerializer, GetProfileSerializer

class ProfilesView(APIView):

    def post(self, request):
        serializer = PostProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def get(self, request):
        profiles = Profile.objects.all()
        serializer = GetProfileSerializer(profiles, many = True)
        return Response(serializer.data)

<<<<<<< Updated upstream
=======
class ProfilesAddressesValidation(APIView):

    def get(self, request, jwt):
        try:
            verifier = VerificationToken()
            validation = verifier.parse_token(jwt)
            if validation["valid"]:
                profile = Profile.objects.get(pk=validation["profile_id"])
                setattr(profile, validation["change_flag"], True)
                profile.save()
                return Response(f'Valid {validation["verify_property"]}', status=HTTP_200_OK)
            else:
                raise Exception
        except Exception:
            return Response("Invalid token", status=HTTP_400_BAD_REQUEST)
>>>>>>> Stashed changes
