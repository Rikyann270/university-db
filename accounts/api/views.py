from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import  IsAuthenticated

from accounts.api.serializers import (
    RegistrationSerializer,
    AccountUpdateSerializers,
    AccountPropertiesSerializers
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