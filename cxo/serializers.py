from rest_framework import  serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


def required(value):
    """Checks if the value is specified or not"""
    if value is None:
        raise serializers.ValidationError('This field is required')


def check(value):
    """Checks if the correct type value specified"""
    if value != "student" and value != "teacher" and value != "admin":
        raise serializers.ValidationError("Wrong Type Specified")


class UserSerializer(serializers.ModelSerializer):
    """For serializing User Model
    type field data necessary to create objects"""
    type = serializers.CharField(validators=[required, check], write_only=True)
    types = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = '__all__'

    def get_types(self, obj):
        names = []
        for group in obj.groups.all():
            names.append(group.name)
        return names


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], password=validated_data['password'],
                                        first_name=validated_data['first_name'],
                                        last_name=validated_data['last_name'])
        return user


