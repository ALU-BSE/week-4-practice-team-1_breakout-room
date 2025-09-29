from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import Rider

User = get_user_model()


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response(data={
            "id": user.id,
            "email": user.email,
            "first_name": user.first_name,
            "user_type": user.user_type,
        })


class RidersListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        riders = User.objects.filter(user_type="rider")
        data = [
            {
                "id": rider.id,
                "email": rider.email,
                "first_name": rider.first_name,
            }
            for rider in riders
        ]
        return Response(data, status=status.HTTP_200_OK)
