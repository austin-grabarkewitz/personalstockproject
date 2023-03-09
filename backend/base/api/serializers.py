from rest_framework.serializers import ModelSerializer
from base.models import FaveTicker

class FavTickerSerializer(ModelSerializer):
    class Meta:
        model = FaveTicker
        fields = '__all__'