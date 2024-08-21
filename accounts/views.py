from django.contrib.auth import logout
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


class LogoutAPIView(APIView):
    """
    API view for user logout
    """
    permission_classes = [AllowAny]

    def post(self, request):
        """
        Handle POST request for user logout

        Args:
            request: The request object

        Returns:
            Response: The response object indicating successful logout
        """
        logout(request)  
        response = Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)
        return response