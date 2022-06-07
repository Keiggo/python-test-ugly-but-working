from djoser.serializers import UserCreateSerializer, UserSerializer as BaseUserSerializer

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ['id', 'first_name', 'last_name', 'email', 'password']


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'first_name', 'last_name', 'email']
