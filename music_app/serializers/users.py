from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
import re

User = get_user_model()

class UserSerializer(serializers.HyperlinkedModelSerializer):
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    username = serializers.CharField(min_length=6, max_length=20,
                                     validators=[UniqueValidator(queryset=User.objects.all())])

    email = serializers.EmailField(style={'input_type': 'email'},
                                    validators=[UniqueValidator(queryset=User.objects.all())])

    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    def validate_username(self, value):
        if not re.match("^[a-z0-9\@\.\+\-\_]*$", value):
            raise serializers.\
                ValidationError('Enter a valid username. '
                                'This value may contain only letters, numbers, and @/./+/-/_ characters.')

        return value

    def validate_password(self, value):
        if value.isalnum() or not any(c.isdigit() for c in value) or value == value.lower():
            raise serializers.ValidationError('Password must contains one upper digit, one number and one symbol.')
        password_validation.validate_password(value, self.instance)

        return value

    class Meta:
        model = User
        fields = ['url', 'first_name', 'last_name', 'username', 'email', 'password']

    def create(self, validated_data):
        validated_data['first_name'] = validated_data['first_name'].capitalize()
        validated_data['last_name'] = validated_data['last_name'].capitalize()
        validated_data['password'] = make_password(validated_data['password'])

        return super(UserSerializer, self).create(validated_data)
