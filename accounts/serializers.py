from rest_framework import serializers
from accounts.models import User

class LoginSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'phone', 'password','email', 'first_name', 'last_name','type')
        read_only_fields = ('id','email', 'first_name', 'last_name')