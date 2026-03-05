from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate



@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        if not user.is_active:
            return Response({"message": "User account is disabled."}, status=status.HTTP_403_FORBIDDEN)

        # For a real application, you should generate and return a token here.
        return Response({"message": "Login successful"})
    else:
        return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)