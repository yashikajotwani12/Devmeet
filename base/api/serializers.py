from rest_framework.serializers import ModelSerializer
from rest_framework.utils import field_mapping
from base.models import Room

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
        