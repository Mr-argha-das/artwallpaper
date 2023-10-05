from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        app_label = 'artwallpaper'
        model = User
        fields = ('id', 'an_login_id','username', 'email', 'gender', 'password', )