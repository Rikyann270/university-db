from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import  IsAuthenticated
from django.contrib.auth import authenticate, login

from accounts.models import Scholar_liked


from accounts.api.serializers import (
    RegistrationSerializer,
    AccountUpdateSerializers,
    AccountPropertiesSerializers,
    AccountLoginSerializers,
    ScholarLikedSerializer,
                                      )
from rest_framework.authtoken.models import Token

@api_view(['POST',])
def registration_view(request):

    if request.method == 'POST':
        
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            accounts = serializer.save()
            data['response'] = "sucessfuly registered"
            data['password'] = accounts.password
            token = Token.objects.get(user=accounts).key
            data['token'] = token
            # data['phone_number'] = accounts.phone_number
  
        else:
            data = serializer.errors
        
        return Response(data)

@api_view(['POST'])
def login_view(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        
        if not username or not password:
            return Response({'error': 'Please provide both username and password.'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)  # Retrieve or create token for the user
            serializer = AccountPropertiesSerializers(user)
            # Retrieve all Scholar_liked entries for the user
            liked_scholars = Scholar_liked.objects.filter(user=user)
            liked_scholars_serializer = ScholarLikedSerializer(liked_scholars, many=True)
            

            return Response({
                'user': serializer.data,
                'token': token.key,
                'liked_scholars': liked_scholars_serializer.data
            })
        else:
            return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)

    
@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def account_properties_view(request):
    try:
        account = request.user
    except Account.DoesNotExit:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = AccountPropertiesSerializers(account)
        return Response(serializer.data)
    

@api_view(['PUT',])
@permission_classes((IsAuthenticated,))
def update_account_view(request):
    try:
        account = request.user
    except Account.DoesNotExit:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = AccountUpdateSerializers(account, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = "Account update success"
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)