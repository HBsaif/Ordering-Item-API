from django.contrib.auth.models import User, Group
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from test_my_API.serializers import ItemOrderSerializer, CharityGetAllSerializer, UserLoginSerializer, CharityLoginSerializer, UserSerializer, GroupSerializer, ItemSerializer, CharityRegistrationSerializer, UserRegistrationSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .models import Item, CharityRegistration, UserRegistration
from django.http import JsonResponse
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

# Create your views here.

@api_view(['GET'])
def get_item(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return JsonResponse({'items': serializer.data})

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_item(request):
    serializer = ItemSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )

@api_view(['GET', 'PUT', 'DELETE'])
def item_details(request, id):
    try:
        item = Item.objects.get(pk=id)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = ItemSerializer(item, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def register_new_charity(request):
    serializer = CharityRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"Status":"Added"}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def register_new_user(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"Status":"Added"}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_new_charity(request):
    serializer = CharityLoginSerializer(data=request.data)
    
    if serializer.is_valid():
        email = serializer.data['Email']
        try:
            Password = list(CharityRegistration.objects.filter(Email=email).values())[0]['Password']
            print(Password)
            if Password == serializer.data['Password']:
                return Response({"Status":"Success"}, status=status.HTTP_202_ACCEPTED)
            else:
                return Response({"Status":"Fail"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"Status":"User Not Found"}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_new_user(request):
    serializer = UserLoginSerializer(data=request.data)
    
    if serializer.is_valid():
        email = serializer.data['Email']
        try:
            Password = list(UserRegistration.objects.filter(Email=email).values())[0]['Password']
            print(Password)
            if Password == serializer.data['Password']:
                return Response({"Status":"Success"}, status=status.HTTP_202_ACCEPTED)
            else:
                return Response({"Status":"Fail"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"Status":"User Not Found"}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_all_charities(request):
    charities = CharityRegistration.objects.all()
    serializer = CharityGetAllSerializer(charities, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def get_all_items_by_email(request):
    email = request.data['Email']
    items = Item.objects.filter(Charity=email)
    serializer = ItemSerializer(items, many=True)

    return Response(serializer.data)


# @api_view(['POST'])
# def order_item(request):
#     serializer = ItemOrderSerializer(data=request.data)
#     if serializer.is_valid():
#         itemId = serializer.data['ItemId']
#         quantity = serializer.data['Quantity']
#         item = Item.objects.filter(ItemId=itemId)
#         if item:
#             if quantity <= item[0].Quantity:
#                 q = Item.objects.filter(ItemId=itemId)
#                 Item.objects.filter(ItemId=itemId) -= quantity
#                 serializer.save()
#                 return Response({"Status":"Ordered"}, status=status.HTTP_201_CREATED)
#             else:
#                 return Response({"Status":"Not enough quantity item"}, status=status.HTTP_400_BAD_REQUEST)

#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def order_item(request):
    serializer = ItemOrderSerializer(data=request.data)
    if serializer.is_valid():
        itemId = serializer.validated_data['ItemId'].ItemId
        print(itemId)
        quantity = serializer.validated_data['Quantity']

        item = get_object_or_404(Item, ItemId=itemId)
        if quantity > item.Quantity:
            return Response({"status":"Not enough quantity item"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            item.Quantity -= quantity
            item.save()
            serializer.save()
            return Response({"status":"Ordered"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)