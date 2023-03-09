from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from base.models import FaveTicker
from rest_framework import status

#------------------------------------------------------------------------------------
#from the simpleJWT Docs 'Customizing token claims'
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

#------------------------------------------------------------------------------------
from .serializers import FavTickerSerializer
from base.models import FaveTicker


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username #grabs the specified attributes of the user model. 'token' here is basically in encripted dictionary
        # ...

        return token
    
class MyTokenObtainPairView(TokenObtainPairView):   #creates a new view for the serialized information that's based off the old template by inheriting the old method ('template')
    serializer_class = MyTokenObtainPairSerializer
    
#------------------------------------------------------------------------------------
#create routes for tokens
@api_view(['Get']) #need the api view to use the Response method. 
def getRoutes(request):
    routes = [
        '/api/token', 
        '/api/token/refresh', 
    ]

    return Response(routes)


###########################################################


#get the user items
# @api_view(['Get'])
# @permission_classes([IsAuthenticated]) #will not allow access to 'http://127.0.0.1:8000/api/faveTickers/' without a token
# def getFavTicker(request):
#     user = request.user
#     ticker = user.faveTick.all()
#     serializer = FavTickerSerializer(ticker, many=True)
#     return Response(serializer.data)


# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def follow_stock(request):
#     symbol = request.data.get('symbol', '')
#     user = request.user
    
    # create a new FaveTicker object for the user with the given symbol
    # fave_ticker = FaveTicker.objects.create(user=user, favTicker=symbol)
    
    # # return a success response
    # serializer = FavTickerSerializer(fave_ticker)
    # return Response(serializer.data, status=status.HTTP_201_CREATED)



###########################################################

@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def tickers(request):

#List all code snippets, or create a new snippet.

    if request.method == 'GET':
        user = request.user
        ticker = user.faveTick.all()
        serializer = FavTickerSerializer(ticker, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = FavTickerSerializer(data = request.data)
        if serializer.is_valid(): #And doesnt exists
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        tickerID=request.data['id']
        ticker_to_delete = FaveTicker.objects.filter(id=tickerID)
        if ticker_to_delete:
            ticker_to_delete.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'error': 'FaveTicker not found'}, status=status.HTTP_404_NOT_FOUND)
            
            



def user_api_view(request):
    user = request.user
    if user.is_authenticated:
        response_data = {
            'username': user.username,
            'user_id': user.id,

            # add other user data as needed
        }
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Not authenticated'}, status=401)

    




    