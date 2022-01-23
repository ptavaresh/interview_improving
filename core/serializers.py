from django.contrib.auth.models import User, Group
from rest_framework import serializers

from core.models import Amount



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class AmountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Amount
        fields = ['amount']

class SearchSerializer(serializers.Serializer):
    amount = serializers.IntegerField()

    def validate_amount(self, value):
        if value < 1 or value > 10000:
            raise serializers.ValidationError('Amount cannot be more than $10000.')
        return value
